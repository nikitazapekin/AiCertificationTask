# Development Environment Setup

Please perform the following development environment setup tasks:

## 1. Dependencies Installation
```bash
npm install
```

## 2. Environment Configuration
- Check if `.env` file exists
- If not, create from template or provide instructions
- Verify required environment variables are set

## 3. Database Setup
- Verify PostgreSQL connection is available
- Check database configuration in environment
- List any required migrations

## 4. Build Verification
```bash
npx nx build backend
```

## 5. Test Verification
```bash
npx nx test backend
```

## 6. Development Server
```bash
npx nx serve backend
```
- Backend should be available at http://localhost:3000
- Swagger documentation at http://localhost:3000/docs

## 7. Project Structure Verification
Verify the following key directories exist:
- `apps/backend/src/`
- `libs/shared/kernel/`
- `libs/shared/database/`
- `libs/shared/logger/`
- `libs/domains/users/`
- `libs/domains/auth/`

## Additional Notes
Arguments: $ARGUMENTS

Provide clear feedback on each step's success or failure.
