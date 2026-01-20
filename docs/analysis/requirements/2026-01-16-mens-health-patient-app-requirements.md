# Men's Health Patient App - Requirements Document

## Overview

A HIPAA-compliant patient-facing healthcare application for a men's health practice. The application integrates with Tebra EHR/PMS and Shopify to provide patients with medication reminders, appointment notifications, lab results visualization, and retail purchasing capabilities.

## Source

- Document: `Men's health QA.md`
- Client Q&A responses and clarification session

## Project Constraints

| Constraint | Value |
|------------|-------|
| Platform | Web-first with mobile companion |
| MVP Scope | Patient app only (no staff features) |
| Compliance | Full HIPAA compliance required |
| Primary EHR | Tebra |
| E-commerce | Shopify integration |

---

## Functional Requirements

### FR-001: User Authentication & Authorization

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-001.1 | Email/password registration | Patients can create accounts with email verification | High |
| FR-001.2 | Multi-factor authentication | MFA required for all logins (HIPAA requirement) | High |
| FR-001.3 | Password reset flow | Secure password reset via email with expiring tokens | High |
| FR-001.4 | Session management | Secure session handling with automatic timeout | High |
| FR-001.5 | Patient-EHR linking | Link app account to Tebra patient record | High |

### FR-002: Medicine Reminder

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-002.1 | Medication sync from Tebra | Pull active prescriptions from Tebra EHR API | High |
| FR-002.2 | Display medication schedule | Show daily/weekly medication schedule with times | High |
| FR-002.3 | Push notifications | Send in-app notifications at scheduled medication times | High |
| FR-002.4 | Medication details view | Display drug name, dosage, instructions, warnings | Medium |
| FR-002.5 | Sync refresh | Manual and automatic refresh of medication data | Medium |

**Note:** No adherence tracking required (per client specification).

### FR-003: Appointment Reminder

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-003.1 | Appointment sync from Tebra | Pull upcoming appointments from Tebra PMS API | High |
| FR-003.2 | Appointment list view | Display upcoming appointments with date, time, provider, location | High |
| FR-003.3 | In-app notifications | Push notifications for appointment reminders (configurable timing) | High |
| FR-003.4 | Appointment details | Show appointment type, provider info, location/directions | Medium |
| FR-003.5 | Calendar integration | Optional export to device calendar | Low |

**Note:** No appointment scheduling/rescheduling in MVP (notifications only).

### FR-004: Lab Results & Graphs

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-004.1 | Lab results sync from Tebra | Pull lab results from Tebra EHR API | High |
| FR-004.2 | Results list view | Display lab results in tabular format with values and reference ranges | High |
| FR-004.3 | Range highlighting | Visual indication of normal/abnormal/critical values | High |
| FR-004.4 | Trend graphs | Charts showing historical values over time for each test type | High |
| FR-004.5 | Result details | Detailed view with test name, value, units, range, date collected | Medium |
| FR-004.6 | Results filtering | Filter by date range, test type, status | Medium |

### FR-005: Retail Purchases (Shopify Integration)

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-005.1 | Product catalog display | Show Shopify products (supplements, medication supplies) | High |
| FR-005.2 | Product search/filter | Search by name, filter by category | Medium |
| FR-005.3 | Shopping cart | Add/remove items, adjust quantities | High |
| FR-005.4 | Checkout via Shopify | Redirect to Shopify checkout or embedded checkout | High |
| FR-005.5 | Order history | Display past orders from Shopify | Medium |
| FR-005.6 | Subscription management | View/manage recurring subscription orders | Medium |

### FR-006: Patient Profile

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-006.1 | View profile information | Display patient demographics from Tebra | Medium |
| FR-006.2 | Notification preferences | Configure reminder timing and frequency | Medium |
| FR-006.3 | Account settings | Change password, manage MFA, logout | High |

---

## Non-Functional Requirements

### NFR-001: Security & Compliance (HIPAA)

| ID | Requirement | Metric/Criteria | Priority |
|----|-------------|-----------------|----------|
| NFR-001.1 | Data encryption at rest | AES-256 encryption for all PHI | High |
| NFR-001.2 | Data encryption in transit | TLS 1.3 for all API communications | High |
| NFR-001.3 | Audit logging | Log all PHI access with user, timestamp, action | High |
| NFR-001.4 | Access controls | Role-based access control, minimum necessary principle | High |
| NFR-001.5 | Session timeout | Auto-logout after 15 minutes of inactivity | High |
| NFR-001.6 | Secure token storage | Use secure storage for auth tokens (Keychain/Keystore) | High |

### NFR-002: Performance

| ID | Requirement | Metric/Criteria | Priority |
|----|-------------|-----------------|----------|
| NFR-002.1 | Page load time | Initial load < 3 seconds on 4G connection | Medium |
| NFR-002.2 | API response time | < 500ms for standard API calls | Medium |
| NFR-002.3 | Offline capability | Cache essential data for offline viewing | Low |

### NFR-003: Reliability

| ID | Requirement | Metric/Criteria | Priority |
|----|-------------|-----------------|----------|
| NFR-003.1 | Availability | 99.5% uptime SLA | High |
| NFR-003.2 | Error handling | Graceful degradation when Tebra/Shopify unavailable | Medium |

---

## Integration Requirements

### INT-001: Tebra EHR/PMS Integration

| Endpoint | Purpose | Data |
|----------|---------|------|
| Patient API | Verify/link patient identity | Demographics, patient ID |
| Medications API | Fetch active prescriptions | Drug name, dosage, schedule |
| Appointments API | Fetch upcoming appointments | Date, time, provider, location |
| Lab Results API | Fetch lab results | Test name, value, range, date |

**Reference:** [Tebra API Documentation](https://helpme.tebra.com/Tebra_PM/12_API_and_Integration/01_Get_Started_with_Tebra_API_Integration)

### INT-002: Shopify Integration

| Integration Point | Purpose |
|-------------------|---------|
| Storefront API | Product catalog, search |
| Checkout API | Cart and checkout flow |
| Customer API | Link Shopify customer to app user |
| Orders API | Order history retrieval |

---

## Business Rules

| ID | Rule | Context |
|----|------|---------|
| BR-001 | Patient must be verified in Tebra before accessing clinical data | Prevents unauthorized access to PHI |
| BR-002 | Medication reminders only show active prescriptions | Expired/discontinued meds excluded |
| BR-003 | Lab results show only finalized results | Draft/pending results not displayed |
| BR-004 | MFA is mandatory, not optional | HIPAA compliance requirement |

---

## Task Breakdown

### Phase 1: Foundation

#### Backend (NestJS)

| Task | Description | Estimated Effort |
|------|-------------|------------------|
| Auth Module | JWT auth with MFA support, session management | Large |
| User Module | Patient registration, profile management | Medium |
| Tebra Integration Service | API client for Tebra EHR/PMS | Large |
| Shopify Integration Service | API client for Shopify Storefront/Checkout | Medium |
| Audit Logging | HIPAA-compliant activity logging | Medium |

#### Entities

| Entity | Properties | Relations |
|--------|------------|-----------|
| User | id, email, passwordHash, mfaSecret, tebraPatientId, shopifyCustomerId, createdAt, updatedAt | has many AuditLogs |
| AuditLog | id, userId, action, resourceType, resourceId, ipAddress, timestamp | belongs to User |
| NotificationPreference | id, userId, medicationReminder, appointmentReminder, reminderLeadTime | belongs to User |

### Phase 2: Core Features

#### Backend Services

| Service | Methods | Purpose |
|---------|---------|---------|
| MedicationService | syncMedications, getMedications, getSchedule | Medication reminder data |
| AppointmentService | syncAppointments, getUpcoming, getDetails | Appointment data |
| LabResultService | syncResults, getResults, getTrends | Lab results and trends |
| NotificationService | scheduleMedicationReminder, scheduleAppointmentReminder | Push notification scheduling |
| ShopifyService | getProducts, getCart, createCheckout, getOrders | E-commerce operations |

#### Controllers

| Controller | Endpoints | Purpose |
|------------|-----------|---------|
| AuthController | POST /auth/register, POST /auth/login, POST /auth/mfa/verify, POST /auth/refresh | Authentication |
| UserController | GET /users/me, PATCH /users/me, GET /users/me/preferences | Profile management |
| MedicationController | GET /medications, GET /medications/schedule | Medication data |
| AppointmentController | GET /appointments, GET /appointments/:id | Appointment data |
| LabResultController | GET /lab-results, GET /lab-results/:id/trends | Lab data |
| ShopifyController | GET /shop/products, POST /shop/checkout, GET /shop/orders | E-commerce |

### Phase 3: Frontend (React Web + React Native Mobile)

#### Web Components

| Component | Purpose |
|-----------|---------|
| LoginPage | Email/password + MFA flow |
| Dashboard | Overview with upcoming meds, appointments, recent labs |
| MedicationList | Daily medication schedule |
| AppointmentList | Upcoming appointments |
| LabResultsView | Results table + trend charts |
| ShopPage | Product grid, cart, checkout |
| ProfilePage | Settings and preferences |

#### Mobile Components

| Component | Purpose |
|-----------|---------|
| Same as web | React Native equivalents with mobile-optimized UX |
| Push notification handling | Native notification integration |

### Phase 4: Testing & Compliance

| Task | Description |
|------|-------------|
| Unit Tests | Service and repository layer tests |
| Integration Tests | API endpoint tests with Tebra/Shopify mocks |
| E2E Tests | Critical user flows |
| Security Audit | HIPAA compliance review |
| Penetration Testing | Security vulnerability assessment |

---

## Gap Analysis / Open Questions

- [ ] **Tebra API access:** Has the practice obtained API credentials and reviewed rate limits?
- [ ] **Shopify plan:** Does current Shopify plan support Storefront API access?
- [ ] **MFA method:** SMS, authenticator app, or both for MFA?
- [ ] **Notification timing:** What default lead times for appointment reminders (1 day, 1 hour, etc.)?
- [ ] **Patient verification:** What is the patient verification flow to link app account to Tebra record?
- [ ] **Terms & Privacy Policy:** Are HIPAA-compliant privacy policy and terms of service prepared?
- [ ] **BAA requirements:** Business Associate Agreements needed with hosting provider, etc.

---

## Future Scope (Not in MVP)

The following were identified as needed but excluded from MVP:

**Staff/Admin Features:**
- Appointment scheduling & management
- Patient registration & intake
- Billing & invoicing
- Insurance claims management
- Facility/resource management
- Clinical charting
- e-Prescribing
- Diagnostics & procedure coding

These should be considered for Phase 2+ as a separate staff web application.

---

## Next Steps

After user approval, proceed with:

1. `/brainstorm` - Refine technical approach and design decisions
2. `/architect` - Make technology and architecture decisions
3. `/writing-plans` - Create detailed implementation plan
