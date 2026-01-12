# Shared Infrastructure Modules

Minimal, reusable infrastructure modules. No business logic.

## Config Module

### env.validation.ts

```typescript
import * as Joi from 'joi';

export const envValidationSchema = Joi.object({
  NODE_ENV: Joi.string()
    .valid('development', 'production', 'test')
    .default('development'),
  PORT: Joi.number().default(3000),
  DATABASE_URL: Joi.string().when('NODE_ENV', {
    is: 'test',
    then: Joi.optional(),
    otherwise: Joi.required(),
  }),
});
```

### config.service.ts

```typescript
import { Injectable } from '@nestjs/common';
import { ConfigService as NestConfigService } from '@nestjs/config';

@Injectable()
export class ConfigService {
  constructor(private readonly configService: NestConfigService) {}

  get port(): number {
    return this.configService.get<number>('PORT', 3000);
  }

  get nodeEnv(): string {
    return this.configService.get<string>('NODE_ENV', 'development');
  }

  get isDevelopment(): boolean {
    return this.nodeEnv === 'development';
  }

  get isProduction(): boolean {
    return this.nodeEnv === 'production';
  }

  get databaseUrl(): string {
    return this.configService.getOrThrow<string>('DATABASE_URL');
  }
}
```

### config.module.ts

```typescript
import { Global, Module } from '@nestjs/common';
import { ConfigModule as NestConfigModule } from '@nestjs/config';
import { ConfigService } from './config.service';
import { envValidationSchema } from './env.validation';

@Global()
@Module({
  imports: [
    NestConfigModule.forRoot({
      isGlobal: true,
      validationSchema: envValidationSchema,
    }),
  ],
  providers: [ConfigService],
  exports: [ConfigService],
})
export class ConfigModule {}
```

## Logger Module

### logger.service.ts

```typescript
import { Injectable, LoggerService as NestLoggerService } from '@nestjs/common';

@Injectable()
export class LoggerService implements NestLoggerService {
  log(message: string, context?: string): void {
    console.log(`[${context || 'App'}] ${message}`);
  }

  error(message: string, trace?: string, context?: string): void {
    console.error(`[${context || 'App'}] ERROR: ${message}`);
    if (trace) console.error(trace);
  }

  warn(message: string, context?: string): void {
    console.warn(`[${context || 'App'}] WARN: ${message}`);
  }

  debug(message: string, context?: string): void {
    console.debug(`[${context || 'App'}] DEBUG: ${message}`);
  }

  verbose(message: string, context?: string): void {
    console.log(`[${context || 'App'}] VERBOSE: ${message}`);
  }
}
```

### logger.module.ts

```typescript
import { Global, Module } from '@nestjs/common';
import { LoggerService } from './logger.service';

@Global()
@Module({
  providers: [LoggerService],
  exports: [LoggerService],
})
export class LoggerModule {}
```

## Error Handling

### error-codes.ts

```typescript
export enum ErrorCode {
  // Generic
  INTERNAL_ERROR = 'INTERNAL_ERROR',
  VALIDATION_ERROR = 'VALIDATION_ERROR',
  NOT_FOUND = 'NOT_FOUND',
  UNAUTHORIZED = 'UNAUTHORIZED',
  FORBIDDEN = 'FORBIDDEN',
  CONFLICT = 'CONFLICT',
  BAD_REQUEST = 'BAD_REQUEST',
}
```

### http-exception.filter.ts

```typescript
import {
  ExceptionFilter,
  Catch,
  ArgumentsHost,
  HttpException,
  HttpStatus,
} from '@nestjs/common';
import { Request, Response } from 'express';
import { ErrorCode } from './error-codes';

@Catch()
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();

    let status = HttpStatus.INTERNAL_SERVER_ERROR;
    let message = 'Internal server error';
    let code = ErrorCode.INTERNAL_ERROR;

    if (exception instanceof HttpException) {
      status = exception.getStatus();
      const exceptionResponse = exception.getResponse();
      message =
        typeof exceptionResponse === 'string'
          ? exceptionResponse
          : (exceptionResponse as any).message || exception.message;
      code = this.mapStatusToErrorCode(status);
    }

    response.status(status).json({
      statusCode: status,
      code,
      message,
      path: request.url,
      timestamp: new Date().toISOString(),
    });
  }

  private mapStatusToErrorCode(status: number): ErrorCode {
    const map: Record<number, ErrorCode> = {
      400: ErrorCode.BAD_REQUEST,
      401: ErrorCode.UNAUTHORIZED,
      403: ErrorCode.FORBIDDEN,
      404: ErrorCode.NOT_FOUND,
      409: ErrorCode.CONFLICT,
      422: ErrorCode.VALIDATION_ERROR,
    };
    return map[status] || ErrorCode.INTERNAL_ERROR;
  }
}
```

## Database Module (TypeORM)

### database.module.ts

```typescript
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigService } from '../config/config.service';

@Module({
  imports: [
    TypeOrmModule.forRootAsync({
      inject: [ConfigService],
      useFactory: (config: ConfigService) => ({
        type: 'postgres',
        url: config.databaseUrl,
        autoLoadEntities: true,
        synchronize: config.isDevelopment, // Never in production
        logging: config.isDevelopment,
      }),
    }),
  ],
})
export class DatabaseModule {}
```

## Database Module (Prisma)

### prisma.service.ts

```typescript
import { Injectable, OnModuleInit, OnModuleDestroy } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  async onModuleInit(): Promise<void> {
    await this.$connect();
  }

  async onModuleDestroy(): Promise<void> {
    await this.$disconnect();
  }
}
```

### database.module.ts (Prisma)

```typescript
import { Global, Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Global()
@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class DatabaseModule {}
```

## Health Module

### health.controller.ts

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller('health')
export class HealthController {
  @Get()
  check() {
    return {
      status: 'ok',
      timestamp: new Date().toISOString(),
    };
  }

  @Get('ready')
  ready() {
    // TODO: Add database/external service checks
    return {
      status: 'ready',
      timestamp: new Date().toISOString(),
    };
  }

  @Get('live')
  live() {
    return {
      status: 'live',
      timestamp: new Date().toISOString(),
    };
  }
}
```

### health.module.ts

```typescript
import { Module } from '@nestjs/common';
import { HealthController } from './health.controller';

@Module({
  controllers: [HealthController],
})
export class HealthModule {}
```

## Bootstrap Files

### main.ts

```typescript
import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';
import { ConfigService } from './shared/config/config.service';
import { LoggerService } from './shared/logger/logger.service';
import { HttpExceptionFilter } from './shared/errors/http-exception.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const config = app.get(ConfigService);
  const logger = app.get(LoggerService);

  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    }),
  );

  app.useGlobalFilters(new HttpExceptionFilter());

  await app.listen(config.port);
  logger.log(`Application running on port ${config.port}`, 'Bootstrap');
}

bootstrap();
```

### http.bootstrap.ts

```typescript
import { INestApplication, ValidationPipe } from '@nestjs/common';
import { HttpExceptionFilter } from '../shared/errors/http-exception.filter';

export function bootstrapHttp(app: INestApplication): void {
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    }),
  );

  app.useGlobalFilters(new HttpExceptionFilter());

  app.enableCors();
}
```

### worker.bootstrap.ts

```typescript
import { INestApplication } from '@nestjs/common';

export function bootstrapWorker(app: INestApplication): void {
  // Worker-specific configuration
  // Add queue processors, scheduled tasks, etc.
}
```

## App Module Template

```typescript
import { Module } from '@nestjs/common';
import { ConfigModule } from './shared/config/config.module';
import { LoggerModule } from './shared/logger/logger.module';
import { DatabaseModule } from './shared/database/database.module';
import { HealthModule } from './shared/health/health.module';
// Import feature modules here

@Module({
  imports: [
    // Shared infrastructure (order matters)
    ConfigModule,
    LoggerModule,
    DatabaseModule,
    HealthModule,

    // Feature modules
    // UsersModule,
    // OrdersModule,
  ],
})
export class AppModule {}
```
