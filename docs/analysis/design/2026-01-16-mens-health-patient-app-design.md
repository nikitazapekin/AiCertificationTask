# Men's Health Patient App - Design Document

## Problem Statement

A men's health practice needs a HIPAA-compliant patient-facing application to improve patient engagement and care coordination. Patients currently lack easy access to their medical information, medication schedules, appointment reminders, and practice-recommended supplements/supplies. The practice uses Tebra EHR/PMS for clinical operations and Shopify for retail product sales, requiring seamless integration between these systems and the patient app.

## Proposed Solution

Build a web-first patient application with mobile companion that provides:
- Secure authentication with MFA (TOTP authenticator app)
- Medication reminders synced from Tebra EHR
- Appointment notifications from Tebra PMS
- Lab results visualization with trend graphs
- Integrated shopping experience with Shopify products
- Full HIPAA compliance with encryption, audit logging, and access controls

The MVP focuses exclusively on patient features, excluding staff/admin functionality for future phases.

## Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
├──────────────────────────────┬──────────────────────────────┤
│      React Web App           │   React Native Mobile App    │
│   (Desktop/Mobile Browser)   │      (iOS/Android)           │
└──────────────────────────────┴──────────────────────────────┘
                               │
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway / Load Balancer               │
│                      (AWS ALB with TLS 1.3)                  │
└─────────────────────────────────────────────────────────────┘
                               │
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                      Backend Layer (NestJS)                  │
├─────────────────────────────────────────────────────────────┤
│  • Auth Module (JWT + TOTP MFA)                             │
│  • User Module (Patient profiles, preferences)              │
│  • Medication Module (Sync + display)                       │
│  • Appointment Module (Sync + display)                      │
│  • Lab Results Module (Sync + trends)                       │
│  • Shopify Module (Products, orders)                        │
│  • Audit Module (HIPAA logging)                             │
└─────────────────────────────────────────────────────────────┘
           │                    │                    │
           ↓                    ↓                    ↓
┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐
│  PostgreSQL DB   │  │   Tebra EHR/PMS  │  │  Shopify Store  │
│  (AWS RDS)       │  │   (REST API)     │  │ (Storefront API)│
└──────────────────┘  └──────────────────┘  └─────────────────┘
```

### Technology Stack

**Frontend:**
- Monorepo structure (Nx or Turborepo)
- Web: React 18+ with TypeScript, React Router, TanStack Query
- Mobile: React Native with TypeScript, React Navigation
- Shared: TypeScript types, API client, utilities, state management logic
- UI: Tailwind CSS (web), NativeWind or React Native Paper (mobile)

**Backend:**
- NestJS with TypeScript
- PostgreSQL (AWS RDS with encryption at rest)
- TypeORM or Prisma for database access
- Passport.js for authentication
- speakeasy for TOTP generation/validation
- node-cron for scheduled sync jobs

**Infrastructure:**
- AWS with HIPAA BAA
- ECS Fargate for container hosting (serverless, auto-scaling)
- RDS PostgreSQL (Multi-AZ, automated backups, encrypted)
- CloudWatch for logging and monitoring
- AWS Secrets Manager for credential storage
- Application Load Balancer with TLS 1.3

**External Services:**
- Tebra EHR/PMS API (periodic sync)
- Shopify Storefront API + Customer API

## Architectural Decisions

### Decision 1: Tebra Integration - Periodic Sync + Caching

**Chosen Approach:** Background sync jobs that periodically fetch data from Tebra and cache in PostgreSQL.

**Rationale:**
- Better user experience (fast response times from local cache)
- Resilience if Tebra API temporarily unavailable
- Medical data doesn't require real-time updates (appointments/labs change infrequently)
- Allows offline viewing of cached data
- Reduces API rate limit concerns

**Implementation:**
- Cron jobs sync data for "active" patients (logged in within last 24 hours)
- Users can manually trigger refresh via pull-to-refresh
- Sync intervals: every 30 minutes for active patients
- Store last sync timestamp per patient per data type

### Decision 2: Patient-EHR Linking - Secure Invite Code

**Chosen Approach:** Staff generates unique invite codes, patients use during registration to link to Tebra record.

**Rationale:**
- HIPAA-compliant (no PII transmission during public registration)
- Staff maintains control over patient access
- Prevents unauthorized account creation
- Instant access once patient has code
- Can be generated in batches or on-demand

**Implementation:**
- Invite code is UUID or secure random token (min 16 chars)
- Stored in database with tebraPatientId, expiresAt, usedAt
- Single-use only, expires after 7 days
- Staff generates via admin interface (future) or manual database insert (MVP)

### Decision 3: MFA - Authenticator App Only (TOTP)

**Chosen Approach:** TOTP-based MFA using authenticator apps (Google Authenticator, Authy, etc.).

**Rationale:**
- Most secure option (no SMS vulnerabilities)
- Works offline
- HIPAA compliance requirement for MFA
- Simpler implementation (no SMS service needed)
- Healthcare context justifies higher security bar

**Implementation:**
- Generate TOTP secret during registration
- Display QR code for easy setup
- Require 6-digit code on every login
- Backup codes for account recovery (10 single-use codes)

### Decision 4: Notifications - In-App Only

**Chosen Approach:** In-app notifications displayed when user opens the application.

**Rationale:**
- Requirements explicitly state "in-app only"
- Simpler implementation (no push notification infrastructure)
- Sufficient for MVP scope
- Can add push notifications in future phase if needed

**Implementation:**
- Backend checks for upcoming medications/appointments
- Display notification badges/banners when user opens app
- Notification preferences stored per user (reminder timing)

### Decision 5: Frontend - Monorepo with Shared Logic

**Chosen Approach:** Monorepo containing React web app + React Native mobile app with shared TypeScript code.

**Rationale:**
- Web-first requirement suggests web experience is critical
- Share TypeScript types, API client, utilities, business logic
- Platform-optimized UI/UX for each target
- Start web-only, add mobile later without duplication
- Tools like Nx make monorepo management straightforward

**Structure:**
```
apps/
  web/          # React web app
  mobile/       # React Native app
packages/
  shared/       # Shared types, utilities
  api-client/   # API client logic
  ui-components/# Shared component logic (not UI)
```

### Decision 6: Data Storage - PostgreSQL Only

**Chosen Approach:** PostgreSQL for all data persistence (user data, synced Tebra data, audit logs).

**Rationale:**
- Need PostgreSQL anyway for audit logs (HIPAA requirement)
- Patient data volume is low (single practice, patient-specific queries)
- PostgreSQL performance sufficient for this scale
- Simpler architecture = faster MVP
- Single database simplifies HIPAA compliance (encryption, backups, access control)

**Schema Strategy:**
- Separate tables for Users, Medications, Appointments, LabResults, AuditLogs
- Use indexed queries for performance (userId, date ranges)
- Can add Redis caching layer later if needed

### Decision 7: Shopify Integration - Storefront API + Redirect

**Chosen Approach:** Fetch products via Storefront API, display in app, redirect to Shopify for checkout.

**Rationale:**
- Clean separation of concerns (healthcare app vs e-commerce)
- Shopify handles PCI compliance, payment processing, tax calculation
- Simpler and more secure than embedded checkout
- Can still display products beautifully in-app
- Retrieve order history via API for display

**Implementation:**
- Use Shopify Storefront API to fetch product catalog
- Display products in app with search/filter
- "Checkout" button redirects to Shopify store URL
- Link Shopify customer ID to app user for order history retrieval

### Decision 8: Sync Strategy - Smart Hybrid

**Chosen Approach:** Fixed-interval sync for active patients + user-triggered pull-to-refresh.

**Rationale:**
- Balance between data freshness and API efficiency
- Most patients check app daily (active subset is manageable)
- Pull-to-refresh gives users control
- Reduces unnecessary Tebra API calls (rate limit friendly)
- Better UX (data usually fresh for active users)

**Implementation:**
- Define "active patient" as logged in within last 24 hours
- Cron job every 30 minutes syncs active patients
- User can manually trigger sync via pull-to-refresh
- Track lastSyncAt timestamp per patient per data type

### Decision 9: Session Management - Sliding Session in Database

**Chosen Approach:** Database-tracked session with sliding window based on actual activity.

**Rationale:**
- HIPAA requires 15 minutes of *inactivity* timeout (not just token expiration)
- Need to track real user activity (clicks, API calls)
- Easy to implement audit logging (HIPAA requirement)
- Can force logout across devices if needed
- Performance acceptable for patient app scale

**Implementation:**
- Session table: id, userId, token, lastActivityAt, expiresAt
- Update lastActivityAt on every authenticated request
- Auto-logout if (now - lastActivityAt) > 15 minutes
- Log session events to audit log

### Decision 10: Infrastructure - AWS with HIPAA BAA

**Chosen Approach:** AWS cloud infrastructure with signed Business Associate Agreement.

**Rationale:**
- Most mature HIPAA compliance program
- BAA available at all tiers
- ECS Fargate for serverless container deployment
- RDS with encryption, automated backups, Multi-AZ
- Large healthcare customer base with proven patterns
- CloudWatch for comprehensive audit logging

**Key Services:**
- ECS Fargate: Backend container hosting
- RDS PostgreSQL: Encrypted database with backups
- ALB: Load balancing with TLS 1.3
- CloudWatch: Logging and monitoring
- Secrets Manager: Credential storage
- S3: Future file storage (encrypted at rest)

## Data Model

### Core Entities

#### User
```typescript
{
  id: UUID (PK)
  email: string (unique, indexed)
  passwordHash: string
  mfaSecret: string (encrypted)
  mfaBackupCodes: string[] (encrypted, hashed)
  tebraPatientId: string (unique, indexed)
  shopifyCustomerId: string (nullable)
  isActive: boolean
  isVerified: boolean
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### Session
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, indexed)
  token: string (unique, indexed)
  lastActivityAt: timestamp (indexed)
  expiresAt: timestamp
  ipAddress: string
  userAgent: string
  createdAt: timestamp
}
```

#### InviteCode
```typescript
{
  id: UUID (PK)
  code: string (unique, indexed)
  tebraPatientId: string (indexed)
  expiresAt: timestamp
  usedAt: timestamp (nullable)
  usedByUserId: UUID (FK -> User, nullable)
  createdAt: timestamp
}
```

#### NotificationPreference
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, unique)
  medicationReminderEnabled: boolean
  appointmentReminderEnabled: boolean
  appointmentReminderLeadTime: number (hours)
  updatedAt: timestamp
}
```

#### Medication
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, indexed)
  tebraMedicationId: string (indexed)
  drugName: string
  dosage: string
  instructions: string
  frequency: string
  startDate: date
  endDate: date (nullable)
  isActive: boolean
  lastSyncAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### Appointment
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, indexed)
  tebraAppointmentId: string (indexed)
  appointmentType: string
  scheduledAt: timestamp (indexed)
  durationMinutes: number
  providerName: string
  locationName: string
  locationAddress: string
  status: enum (scheduled, completed, cancelled)
  lastSyncAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### LabResult
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, indexed)
  tebraLabResultId: string (indexed)
  testName: string (indexed)
  testCode: string
  resultValue: string
  resultUnit: string
  referenceRangeLow: string (nullable)
  referenceRangeHigh: string (nullable)
  status: enum (normal, abnormal, critical)
  collectedAt: timestamp (indexed)
  resultedAt: timestamp
  lastSyncAt: timestamp
  createdAt: timestamp
  updatedAt: timestamp
}
```

#### AuditLog
```typescript
{
  id: UUID (PK)
  userId: UUID (FK -> User, indexed, nullable)
  action: string (indexed, e.g., "LOGIN", "VIEW_LAB_RESULTS")
  resourceType: string (e.g., "LabResult", "Medication")
  resourceId: UUID (nullable)
  ipAddress: string
  userAgent: string
  success: boolean
  errorMessage: string (nullable)
  timestamp: timestamp (indexed)
}
```

### Indexes

**Critical for performance:**
- User: email, tebraPatientId
- Session: userId, token, lastActivityAt
- InviteCode: code, tebraPatientId
- Medication: userId, tebraMedicationId, isActive
- Appointment: userId, scheduledAt, tebraAppointmentId
- LabResult: userId, testName, collectedAt
- AuditLog: userId, action, timestamp

### Relationships

- User 1:N Session
- User 1:1 NotificationPreference
- User 1:N Medication
- User 1:N Appointment
- User 1:N LabResult
- User 1:N AuditLog

## API Design

### Authentication Endpoints

#### POST /auth/register
**Request:**
```json
{
  "email": "patient@example.com",
  "password": "SecureP@ssw0rd",
  "inviteCode": "abc123-def456-ghi789"
}
```

**Response:**
```json
{
  "userId": "uuid",
  "mfaSetupRequired": true,
  "mfaSecret": "BASE32SECRET",
  "mfaQrCodeUrl": "otpauth://totp/..."
}
```

#### POST /auth/setup-mfa
**Request:**
```json
{
  "userId": "uuid",
  "totpCode": "123456"
}
```

**Response:**
```json
{
  "success": true,
  "backupCodes": ["code1", "code2", ...]
}
```

#### POST /auth/login
**Request:**
```json
{
  "email": "patient@example.com",
  "password": "SecureP@ssw0rd"
}
```

**Response:**
```json
{
  "mfaRequired": true,
  "tempToken": "temporary-token-for-mfa"
}
```

#### POST /auth/mfa-verify
**Request:**
```json
{
  "tempToken": "temporary-token",
  "totpCode": "123456"
}
```

**Response:**
```json
{
  "accessToken": "jwt-token",
  "user": {
    "id": "uuid",
    "email": "patient@example.com"
  }
}
```

#### POST /auth/logout
**Headers:** Authorization: Bearer {token}

**Response:**
```json
{
  "success": true
}
```

### User Endpoints

#### GET /users/me
**Headers:** Authorization: Bearer {token}

**Response:**
```json
{
  "id": "uuid",
  "email": "patient@example.com",
  "tebraPatientId": "tebra123",
  "createdAt": "2026-01-16T00:00:00Z"
}
```

#### PATCH /users/me/preferences
**Headers:** Authorization: Bearer {token}

**Request:**
```json
{
  "medicationReminderEnabled": true,
  "appointmentReminderEnabled": true,
  "appointmentReminderLeadTime": 24
}
```

**Response:**
```json
{
  "success": true,
  "preferences": { ... }
}
```

### Medication Endpoints

#### GET /medications
**Headers:** Authorization: Bearer {token}

**Query params:** ?refresh=true (optional, triggers manual sync)

**Response:**
```json
{
  "medications": [
    {
      "id": "uuid",
      "drugName": "Testosterone Cypionate",
      "dosage": "200mg/ml",
      "instructions": "Inject 0.5ml intramuscularly",
      "frequency": "Weekly",
      "startDate": "2026-01-01",
      "isActive": true,
      "lastSyncAt": "2026-01-16T12:00:00Z"
    }
  ],
  "lastSyncAt": "2026-01-16T12:00:00Z"
}
```

#### GET /medications/schedule
**Headers:** Authorization: Bearer {token}

**Query params:** ?date=2026-01-16 (optional, defaults to today)

**Response:**
```json
{
  "date": "2026-01-16",
  "schedule": [
    {
      "time": "08:00",
      "medications": [
        {
          "id": "uuid",
          "drugName": "Anastrozole",
          "dosage": "0.5mg",
          "instructions": "Take with food"
        }
      ]
    }
  ]
}
```

### Appointment Endpoints

#### GET /appointments
**Headers:** Authorization: Bearer {token}

**Query params:** ?refresh=true (optional)

**Response:**
```json
{
  "appointments": [
    {
      "id": "uuid",
      "appointmentType": "Follow-up Visit",
      "scheduledAt": "2026-01-20T10:00:00Z",
      "durationMinutes": 30,
      "providerName": "Dr. Smith",
      "locationName": "Main Clinic",
      "locationAddress": "123 Health St, City, ST 12345",
      "status": "scheduled"
    }
  ],
  "lastSyncAt": "2026-01-16T12:00:00Z"
}
```

#### GET /appointments/:id
**Headers:** Authorization: Bearer {token}

**Response:**
```json
{
  "id": "uuid",
  "appointmentType": "Follow-up Visit",
  "scheduledAt": "2026-01-20T10:00:00Z",
  "durationMinutes": 30,
  "providerName": "Dr. Smith",
  "locationName": "Main Clinic",
  "locationAddress": "123 Health St, City, ST 12345",
  "status": "scheduled",
  "notes": "Bring recent lab work"
}
```

### Lab Results Endpoints

#### GET /lab-results
**Headers:** Authorization: Bearer {token}

**Query params:**
- ?refresh=true (optional)
- ?startDate=2025-01-01&endDate=2026-01-16 (optional)
- ?testName=Testosterone (optional)

**Response:**
```json
{
  "results": [
    {
      "id": "uuid",
      "testName": "Testosterone, Total",
      "testCode": "TEST001",
      "resultValue": "650",
      "resultUnit": "ng/dL",
      "referenceRangeLow": "300",
      "referenceRangeHigh": "1000",
      "status": "normal",
      "collectedAt": "2026-01-10T08:00:00Z",
      "resultedAt": "2026-01-11T14:00:00Z"
    }
  ],
  "lastSyncAt": "2026-01-16T12:00:00Z"
}
```

#### GET /lab-results/trends/:testName
**Headers:** Authorization: Bearer {token}

**Query params:** ?months=6 (optional, defaults to 12)

**Response:**
```json
{
  "testName": "Testosterone, Total",
  "unit": "ng/dL",
  "referenceRangeLow": "300",
  "referenceRangeHigh": "1000",
  "dataPoints": [
    {
      "date": "2025-07-15",
      "value": "520"
    },
    {
      "date": "2025-10-10",
      "value": "580"
    },
    {
      "date": "2026-01-10",
      "value": "650"
    }
  ]
}
```

### Shopify Endpoints

#### GET /shop/products
**Headers:** Authorization: Bearer {token}

**Query params:**
- ?search=vitamin (optional)
- ?category=supplements (optional)
- ?page=1&limit=20 (optional)

**Response:**
```json
{
  "products": [
    {
      "id": "shopify-product-id",
      "title": "Men's Multivitamin",
      "description": "Complete daily multivitamin...",
      "price": "29.99",
      "currency": "USD",
      "imageUrl": "https://...",
      "category": "supplements"
    }
  ],
  "totalCount": 45,
  "page": 1,
  "pageSize": 20
}
```

#### GET /shop/products/:id
**Headers:** Authorization: Bearer {token}

**Response:**
```json
{
  "id": "shopify-product-id",
  "title": "Men's Multivitamin",
  "description": "Complete daily multivitamin...",
  "price": "29.99",
  "currency": "USD",
  "images": ["https://...", "https://..."],
  "variants": [
    {
      "id": "variant-id",
      "title": "60 capsules",
      "price": "29.99"
    }
  ],
  "category": "supplements"
}
```

#### POST /shop/checkout
**Headers:** Authorization: Bearer {token}

**Request:**
```json
{
  "items": [
    {
      "variantId": "shopify-variant-id",
      "quantity": 2
    }
  ]
}
```

**Response:**
```json
{
  "checkoutUrl": "https://store.myshopify.com/checkout/...",
  "expiresAt": "2026-01-16T13:00:00Z"
}
```

#### GET /shop/orders
**Headers:** Authorization: Bearer {token}

**Query params:** ?page=1&limit=10 (optional)

**Response:**
```json
{
  "orders": [
    {
      "id": "shopify-order-id",
      "orderNumber": "#1001",
      "createdAt": "2026-01-10T12:00:00Z",
      "totalPrice": "59.98",
      "currency": "USD",
      "status": "fulfilled",
      "items": [
        {
          "title": "Men's Multivitamin",
          "quantity": 2,
          "price": "29.99"
        }
      ]
    }
  ],
  "totalCount": 5,
  "page": 1
}
```

## Error Handling

### Error Response Format

All API errors follow consistent format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": { ... } // Optional additional context
  }
}
```

### HTTP Status Codes

- 200: Success
- 201: Created
- 400: Bad Request (validation errors)
- 401: Unauthorized (missing/invalid token)
- 403: Forbidden (insufficient permissions)
- 404: Not Found
- 429: Too Many Requests (rate limiting)
- 500: Internal Server Error
- 503: Service Unavailable (Tebra/Shopify down)

### Error Categories

#### Authentication Errors (401)
- INVALID_CREDENTIALS: Email/password incorrect
- MFA_REQUIRED: MFA verification needed
- INVALID_MFA_CODE: TOTP code incorrect
- SESSION_EXPIRED: Session timeout (15min inactivity)
- INVALID_TOKEN: JWT token invalid/expired

#### Authorization Errors (403)
- ACCOUNT_NOT_VERIFIED: Email not verified
- ACCOUNT_DISABLED: User account disabled
- TEBRA_LINK_REQUIRED: Patient not linked to Tebra

#### Validation Errors (400)
- INVALID_EMAIL: Email format invalid
- WEAK_PASSWORD: Password doesn't meet requirements
- INVALID_INVITE_CODE: Invite code not found/expired/used
- MISSING_REQUIRED_FIELD: Required field missing

#### External Service Errors (503)
- TEBRA_UNAVAILABLE: Tebra API down/timeout
- SHOPIFY_UNAVAILABLE: Shopify API down/timeout
- SYNC_FAILED: Data sync failed (with retry mechanism)

### Error Recovery Strategies

**Session Timeout:**
- Client detects 401 with SESSION_EXPIRED
- Redirect to login page
- Preserve intended destination for post-login redirect

**External Service Failures:**
- Return 503 with cached data if available
- Display warning: "Unable to refresh data, showing last sync from [timestamp]"
- Auto-retry failed sync in background
- Log failures for monitoring

**Validation Errors:**
- Return specific field-level errors
- Client displays inline validation messages
- No retry (user must correct input)

**Rate Limiting:**
- Return 429 with Retry-After header
- Client implements exponential backoff
- Display user-friendly message

## Security Considerations

### HIPAA Compliance Requirements

#### Data Encryption
- **At Rest:** AES-256 encryption for all database fields containing PHI
  - RDS encryption enabled
  - Sensitive fields (mfaSecret, backupCodes) double-encrypted at application layer
- **In Transit:** TLS 1.3 for all API communications
  - HTTPS only, no HTTP allowed
  - Certificate pinning in mobile app

#### Access Controls
- **Authentication:** JWT tokens with 15-minute inactivity timeout
- **Authorization:** User can only access their own data (userId-based filtering)
- **Minimum Necessary:** API endpoints return only required data
- **Session Management:** Database-tracked sessions with activity monitoring

#### Audit Logging
- Log all PHI access with:
  - userId (who)
  - action (what)
  - resourceType + resourceId (which resource)
  - timestamp (when)
  - ipAddress + userAgent (where/how)
  - success/failure status
- Audit logs immutable (append-only)
- Retention: 7 years (HIPAA requirement)
- Regular audit log reviews

#### Business Associate Agreements (BAA)
Required with:
- AWS (hosting provider) ✓
- Tebra (EHR/PMS vendor) - verify if needed
- Any other service handling PHI

### Authentication & Authorization

**Password Requirements:**
- Minimum 12 characters
- Must contain: uppercase, lowercase, number, special character
- Bcrypt hashing with salt rounds >= 12
- Password history (prevent reuse of last 5 passwords)

**MFA (TOTP):**
- 6-digit codes, 30-second time window
- Rate limiting: max 5 attempts per 5 minutes
- Backup codes: 10 single-use codes, hashed in database
- Recovery flow requires email verification

**Session Security:**
- JWT stored in httpOnly cookie (web) or secure storage (mobile)
- CSRF protection for web (double-submit cookie pattern)
- Session invalidation on password change
- Automatic logout on 15 minutes inactivity
- Single concurrent session per user (logout on new login)

### API Security

**Rate Limiting:**
- Authentication endpoints: 5 requests/minute per IP
- Data endpoints: 100 requests/minute per user
- Sync endpoints: 10 requests/minute per user

**Input Validation:**
- All inputs validated against schema (class-validator)
- SQL injection prevention (parameterized queries via ORM)
- XSS prevention (sanitize outputs)
- File upload validation (if added later)

**CORS Configuration:**
- Whitelist only production domains
- Credentials allowed for authenticated requests
- No wildcard origins

### Data Privacy

**PHI Identification:**
Clear understanding of what constitutes PHI in this app:
- Medications (drug names, dosages)
- Appointments (dates, provider names)
- Lab results (test names, values)
- User demographics (from Tebra)

**Data Minimization:**
- Only sync necessary data from Tebra
- Don't store full EHR records, only display-needed fields
- Shopify data (orders) is not PHI but still secure

**User Rights:**
- Account deletion (GDPR/CCPA compliance)
- Data export (provide copy of user's data)
- Access logs (users can view their audit trail)

## Testing Strategy

### Unit Tests

**Coverage Target:** 80% minimum

**Focus Areas:**
- Service layer business logic
- Utility functions (date parsing, validation)
- TOTP generation/validation
- Password hashing/verification
- Data transformation (Tebra API → internal models)

**Tools:**
- Jest for test runner
- ts-mockito or jest.mock for mocking

**Example:**
```typescript
describe('MedicationService', () => {
  it('should filter out inactive medications', () => {
    // Test business logic
  });

  it('should parse Tebra medication frequency correctly', () => {
    // Test data transformation
  });
});
```

### Integration Tests

**Coverage:** All API endpoints

**Focus Areas:**
- Authentication flows (register, login, MFA, logout)
- CRUD operations with database
- External API mocking (Tebra, Shopify)
- Error handling and status codes
- Authorization (user can only access own data)

**Tools:**
- Supertest for HTTP testing
- Test database (PostgreSQL Docker container)
- Nock for HTTP mocking

**Example:**
```typescript
describe('GET /medications', () => {
  it('should return 401 without auth token', () => {
    // Test auth requirement
  });

  it('should return only current user medications', () => {
    // Test authorization
  });
});
```

### E2E Tests

**Coverage:** Critical user flows

**Focus Areas:**
- Complete registration flow (with MFA setup)
- Login flow (with MFA verification)
- View medications/appointments/labs
- Trigger manual sync
- Shopify checkout flow (redirect)
- Session timeout behavior

**Tools:**
- Playwright or Cypress
- Test against staging environment

**Example Flows:**
1. New user registration → MFA setup → login → view dashboard
2. Existing user login → view lab results → check trends
3. User login → browse products → initiate checkout (redirect to Shopify)

### Security Testing

**Penetration Testing:**
- Conduct before production launch
- Focus on authentication, authorization, injection attacks
- Test session management and timeout
- Verify encryption implementation

**HIPAA Compliance Audit:**
- Review all PHI handling
- Verify audit logging completeness
- Check encryption at rest and in transit
- Validate access controls

**Automated Security Scanning:**
- Dependabot for dependency vulnerabilities
- OWASP ZAP or similar for web app scanning
- SonarQube for code quality and security issues

## Implementation Phases

### Phase 1: Foundation (Weeks 1-2)

**Backend:**
- NestJS project setup with TypeORM/Prisma
- PostgreSQL schema implementation
- Authentication module (registration, login, MFA)
- Session management
- Audit logging infrastructure
- Basic error handling

**Frontend:**
- Monorepo setup (Nx/Turborepo)
- React web app scaffold
- Shared package setup (types, API client)
- Authentication UI (register, login, MFA)
- Protected route handling

**Infrastructure:**
- AWS account setup with HIPAA BAA
- RDS PostgreSQL instance (encrypted)
- ECS Fargate configuration
- CI/CD pipeline (GitHub Actions)

**Deliverables:**
- User can register with invite code
- User can set up TOTP MFA
- User can login with email/password + TOTP
- Session timeout works correctly
- All auth actions logged

### Phase 2: Tebra Integration (Weeks 3-4)

**Backend:**
- Tebra API client implementation
- Medication sync service
- Appointment sync service
- Lab results sync service
- Cron jobs for periodic sync
- Manual refresh endpoints

**Frontend:**
- Dashboard page
- Medication list view
- Appointment list view
- Lab results table view
- Lab results trend charts (Chart.js or Recharts)
- Pull-to-refresh functionality

**Deliverables:**
- Medications sync from Tebra and display
- Appointments sync from Tebra and display
- Lab results sync from Tebra with trend graphs
- Users can manually trigger refresh
- Sync status indicators (last sync time)

### Phase 3: Shopify Integration (Week 5)

**Backend:**
- Shopify Storefront API client
- Product catalog endpoints
- Checkout URL generation
- Order history retrieval
- Link Shopify customer to user

**Frontend:**
- Shop page (product grid)
- Product search and filtering
- Product detail view
- Checkout redirect flow
- Order history view

**Deliverables:**
- Users can browse products
- Users can search/filter products
- Checkout redirects to Shopify
- Order history displays in app

### Phase 4: Refinement & Testing (Week 6)

**Backend:**
- Notification preferences API
- User profile management
- Error handling improvements
- Performance optimization
- Security hardening

**Frontend:**
- Profile/settings page
- Notification preferences UI
- Error state handling
- Loading states and skeletons
- Responsive design polish

**Testing:**
- Unit test coverage
- Integration test suite
- E2E critical flows
- Security audit

**Deliverables:**
- Complete test coverage
- All critical bugs fixed
- Performance benchmarks met
- Security audit passed

### Phase 5: Mobile App (Weeks 7-8)

**Mobile:**
- React Native project setup
- Reuse shared packages
- Implement mobile UI components
- Native secure storage integration
- Test on iOS and Android devices

**Deliverables:**
- Mobile app feature parity with web
- Submitted to app stores (TestFlight/beta)

### Phase 6: Production Launch (Week 9)

**Infrastructure:**
- Production environment setup
- SSL certificates configured
- Monitoring and alerting (CloudWatch)
- Backup and disaster recovery testing

**Deployment:**
- Staging deployment and testing
- Production deployment
- Smoke tests
- User acceptance testing

**Documentation:**
- User guide
- Privacy policy and terms of service
- Admin documentation (invite code generation)

**Deliverables:**
- Production system live
- Monitoring operational
- User documentation available

## Open Questions

### Technical Questions

1. **Tebra API Access:**
   - Has the practice obtained API credentials?
   - What are the rate limits?
   - Does Tebra API support webhooks for real-time updates?
   - What is the data freshness SLA from Tebra?

2. **Shopify Plan:**
   - Does current Shopify plan support Storefront API access?
   - Is there an existing Shopify customer database to link?
   - Should app users get automatic discounts (if so, via discount codes)?

3. **Patient Verification:**
   - Who will generate invite codes (staff workflow)?
   - Should invite codes be batch-generated or on-demand?
   - What is the process if a patient loses their invite code?

4. **Notification Timing:**
   - What default lead times for appointment reminders (24h, 1h)?
   - What times should medication reminders default to?
   - Should reminders have snooze functionality?

5. **Session Management:**
   - Should users be logged out across all devices on password change?
   - Should there be a "remember me" option (extends session)?
   - How to handle session conflicts (multiple devices)?

### Business Questions

6. **Compliance:**
   - Are HIPAA-compliant privacy policy and terms of service prepared?
   - Has legal review been completed for BAA requirements?
   - What is the data retention policy (beyond 7-year audit logs)?

7. **User Support:**
   - What is the support process for MFA issues (lost device)?
   - Who handles invite code requests from patients?
   - What is the escalation path for technical issues?

8. **Future Scope:**
   - Timeline for push notifications (if desired post-MVP)?
   - Timeline for mobile app release?
   - When should staff/admin features be considered?

9. **Testing:**
   - Will real patients be involved in UAT?
   - What is the beta testing plan?
   - How many test patients needed for staging environment?

### Infrastructure Questions

10. **AWS Setup:**
    - Who owns the AWS account?
    - What is the backup retention policy?
    - What are the disaster recovery RTO/RPO requirements?

11. **Monitoring:**
    - Who receives production alerts?
    - What are the on-call expectations?
    - What monitoring metrics are critical (uptime, response time, error rate)?

## Next Steps

1. **Resolve Open Questions** - Schedule stakeholder meeting to address all open questions
2. **AWS Setup** - Create AWS account, sign HIPAA BAA, configure initial infrastructure
3. **Tebra API Access** - Obtain API credentials, review documentation, test connectivity
4. **Shopify Configuration** - Verify API access, create test products, configure customer accounts
5. **Create Implementation Plan** - Use `/writing-plans` to break down design into detailed tasks

---

**Document Version:** 1.0
**Last Updated:** 2026-01-16
**Authors:** Requirements Analyst + Brainstorming Session
**Status:** Ready for Architecture Review
