# Men's Health Patient App - Architecture Review

## Overview

This document reviews and validates the architectural decisions made during the design phase for the HIPAA-compliant patient-facing healthcare application.

## Architecture Validation

### Module Placement Decisions

| Module | Location | Rationale | Status |
|--------|----------|-----------|--------|
| Auth | `src/auth/` | Core authentication, MFA, sessions - standalone module | ✅ Correct |
| Users | `src/users/` | Patient profiles, preferences | ✅ Correct |
| Medications | `src/medications/` | Domain-specific medication data | ✅ Correct |
| Appointments | `src/appointments/` | Domain-specific appointment data | ✅ Correct |
| Lab Results | `src/lab-results/` | Domain-specific lab data | ✅ Correct |
| Shop | `src/shop/` | Shopify integration for products/orders | ✅ Correct |
| Audit | `src/audit/` | Cross-cutting HIPAA logging | ✅ Correct |
| Integrations | `src/integrations/tebra/` | External API client | ✅ Correct |

### Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Presentation Layer                                           │
│ - Controllers (HTTP endpoints)                               │
│ - DTOs (Request/Response validation)                         │
│ - Guards (JWT Auth, Rate Limiting)                           │
├─────────────────────────────────────────────────────────────┤
│ Service Layer                                                │
│ - Business logic                                             │
│ - Tebra sync orchestration                                   │
│ - Data transformation                                        │
├─────────────────────────────────────────────────────────────┤
│ Data Access Layer                                            │
│ - TypeORM Repositories                                       │
│ - Entities                                                   │
│ - Database queries                                           │
└─────────────────────────────────────────────────────────────┘
```

**Dependency Flow:** Controller → Service → Repository ✅

### Pattern Choices

| Pattern | Applied To | Rationale |
|---------|-----------|-----------|
| Repository Pattern | All entities | TypeORM provides built-in repository, abstracts DB |
| Service Layer | Business logic | Separates HTTP concerns from business rules |
| DTO Pattern | All endpoints | Validates input, shapes output, prevents over-posting |
| Strategy Pattern | JWT Auth | Passport.js strategy for flexible auth |
| Module Pattern | All features | NestJS modules for encapsulation |
| Cron Jobs | Data sync | Periodic Tebra sync for active patients |

## Entity Relationships Review

### ER Diagram

```
┌─────────────┐     ┌─────────────────────┐     ┌─────────────┐
│   User      │──1:N│   Session           │     │ InviteCode  │
│             │     │                     │     │             │
│ id          │     │ userId (FK)         │     │ code        │
│ email       │     │ token               │     │ tebraId     │
│ passwordHash│     │ lastActivityAt      │     │ usedByUserId│
│ mfaSecret   │     │ expiresAt           │     │ expiresAt   │
│ tebraId     │     └─────────────────────┘     └─────────────┘
│ shopifyId   │
└──────┬──────┘
       │
       ├─────1:1─────┐
       │             │
       ▼             ▼
┌─────────────┐ ┌───────────────────────┐
│ NotifPref   │ │     AuditLog          │
│             │ │                       │
│ userId (FK) │ │ userId (FK, nullable) │
│ medEnabled  │ │ action                │
│ apptEnabled │ │ resourceType          │
│ leadTime    │ │ timestamp             │
└─────────────┘ └───────────────────────┘
       │
       ├─────1:N─────┬─────1:N─────┬─────1:N─────┐
       │             │             │             │
       ▼             ▼             ▼             ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Medication  │ │ Appointment │ │  LabResult  │
│             │ │             │ │             │
│ userId (FK) │ │ userId (FK) │ │ userId (FK) │
│ tebraMedId  │ │ tebraApptId │ │ tebraLabId  │
│ drugName    │ │ scheduledAt │ │ testName    │
│ dosage      │ │ providerName│ │ resultValue │
│ frequency   │ │ status      │ │ status      │
│ isActive    │ │ lastSyncAt  │ │ collectedAt │
│ lastSyncAt  │ └─────────────┘ │ lastSyncAt  │
└─────────────┘                 └─────────────┘
```

### Relationship Validation

| Relationship | Type | Implementation | Status |
|--------------|------|----------------|--------|
| User → Session | 1:N | ManyToOne in Session | ✅ |
| User → NotificationPreference | 1:1 | OneToOne with FK | ✅ |
| User → Medication | 1:N | ManyToOne in Medication | ✅ |
| User → Appointment | 1:N | ManyToOne in Appointment | ✅ |
| User → LabResult | 1:N | ManyToOne in LabResult | ✅ |
| User → AuditLog | 1:N | ManyToOne (nullable) | ✅ |
| InviteCode → User | N:1 | Optional FK | ✅ |

## Security Architecture Review

### HIPAA Compliance Checklist

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Data at Rest Encryption | AWS RDS encryption (AES-256) | ✅ |
| Data in Transit Encryption | TLS 1.3 via ALB | ✅ |
| MFA | TOTP authenticator app | ✅ |
| Session Timeout | 15-min inactivity (sliding window in DB) | ✅ |
| Audit Logging | AuditLog entity, all PHI access logged | ✅ |
| Access Control | JWT + user-scoped queries | ✅ |
| Password Policy | 12+ chars, complexity, bcrypt (12 rounds) | ✅ |
| Backup | RDS automated backups | ✅ |
| BAA | AWS HIPAA BAA | ✅ Required |

### Authentication Flow

```
1. Register with Invite Code
   └─► Validate invite → Create user → Generate MFA secret → Return QR

2. Setup MFA
   └─► Verify TOTP code → Enable MFA → Generate backup codes

3. Login
   └─► Verify email/password → Return temp token (mfaRequired: true)

4. MFA Verify
   └─► Verify temp token → Verify TOTP → Create session → Return JWT

5. Authenticated Request
   └─► JWT in header → Validate session → Check 15-min inactivity
       └─► Update lastActivityAt → Continue OR throw SESSION_EXPIRED
```

### Session Security Analysis

**Chosen: Sliding Session in Database**

| Aspect | Implementation | Risk Mitigation |
|--------|----------------|-----------------|
| Token Storage | httpOnly cookie (web), secure storage (mobile) | XSS protection |
| Session Tracking | DB table with lastActivityAt | True inactivity detection |
| Invalidation | Delete session row | Immediate logout |
| Concurrent Sessions | One active session per user | Reduced attack surface |
| Audit Trail | Session creation/destruction logged | Forensic capability |

**Performance Impact:** ~1 DB query per authenticated request (acceptable for patient app scale)

## Scalability Considerations

### Current Design Limitations

| Concern | Current State | Future Mitigation |
|---------|---------------|-------------------|
| Database Load | All data in PostgreSQL | Add Redis cache if needed |
| Sync Jobs | Cron-based polling | Add webhooks if Tebra supports |
| Session Validation | DB hit per request | Redis session store at scale |
| File Storage | Not implemented | S3 with encryption for future |

### Scaling Strategy

**Phase 1 (Current - MVP):**
- Single ECS task (auto-scaling 1-3)
- RDS PostgreSQL Single-AZ (sufficient for patient volume)
- No caching layer

**Phase 2 (If needed):**
- Add Redis ElastiCache for sessions
- RDS Multi-AZ for high availability
- CloudFront CDN for static assets

**Phase 3 (Staff features):**
- Separate staff-facing backend service
- Read replicas for reporting
- Event-driven sync with SQS

### Load Estimates

| Metric | Estimate | Capacity |
|--------|----------|----------|
| Active patients | ~500-1000 | Sufficient |
| Concurrent users | ~50-100 peak | Sufficient |
| API requests/min | ~500-1000 | Sufficient |
| Database size | ~1-5 GB | RDS minimum |

## Key Architectural Decisions Summary

| Decision | Choice | Confidence | Reversibility |
|----------|--------|------------|---------------|
| Tebra Integration | Periodic sync + cache | High | Medium (can add webhooks) |
| Patient Linking | Invite code | High | Low (core auth flow) |
| MFA | TOTP only | High | Medium (can add SMS later) |
| Notifications | In-app only | Medium | High (can add push later) |
| Frontend | Monorepo (React + RN) | High | Low (significant rework) |
| Database | PostgreSQL only | High | Medium (can add Redis) |
| Shopify | Storefront API + redirect | High | High (can embed later) |
| Sync Strategy | Smart hybrid | High | High (config change) |
| Sessions | Sliding DB session | High | Medium (can add Redis) |
| Infrastructure | AWS with HIPAA BAA | High | Low (significant migration) |

## Risk Assessment

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Tebra API unavailable | Medium | High | Cache + graceful degradation |
| Session table growth | Low | Low | Periodic cleanup job |
| MFA lockout | Low | Medium | Backup codes + support process |
| Data sync conflicts | Low | Low | Tebra as source of truth |

### Security Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Token theft | Low | High | httpOnly cookies, short expiry |
| Brute force | Low | Medium | Rate limiting, account lockout |
| SQL injection | Very Low | Critical | TypeORM parameterized queries |
| XSS | Very Low | High | React escaping, CSP headers |

## Recommendations

### Immediate (Before Implementation)

1. **Verify Tebra API Access** - Obtain credentials, test endpoints
2. **Verify Shopify Plan** - Confirm Storefront API access
3. **AWS HIPAA BAA** - Sign before storing any PHI
4. **Security Headers** - Add helmet.js for HTTP security headers

### Post-MVP Enhancements

1. **Push Notifications** - Add Firebase Cloud Messaging
2. **Offline Mode** - Service worker for cached data access
3. **Analytics** - Anonymous usage tracking for UX improvements
4. **Staff Portal** - Separate web app for admin functions

## Conclusion

The architecture is **well-designed for the MVP scope** with appropriate patterns for a HIPAA-compliant healthcare application. The layered architecture follows NestJS best practices, and the security model addresses HIPAA requirements.

**Architecture Status:** ✅ Approved for implementation

---

## Next Steps

**Next by flow:** `/api-designer` - Design detailed REST API specifications with Swagger/OpenAPI

**Alternatives:**
- `/executing-plans` - Start implementing the plan directly
- `/git-worktrees` - Create isolated workspace before implementation

---

**Document Version:** 1.0
**Last Updated:** 2026-01-16
**Status:** Approved
