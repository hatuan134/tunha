# PHASE 0 AUDIT REPORT

## Status

PARTIAL / BLOCKED

## Repository Inventory

Repository được audit: `hatuan134/tunha`.

Trạng thái ban đầu: repository trống, chưa có source code, migration, test, Docker, tài liệu kỹ thuật hay CI.

## Requirement Inventory

Master Prompt V2.0 xác định phạm vi FR-01 → FR-11, nhưng repository hiện chưa chứa:

- Phase1_QuanLyKho_AI_HoanThien.docx
- SRS / Requirement Specification
- Use Case specification
- ERD / Data Dictionary
- Test Specification TC-01 → TC-24
- Stitch UI

Vì vậy chưa thể hoàn thành traceability đầy đủ `FR → UC → Business Rule → Data → API → UI → Test`.

## Permission Matrix

BLOCKED theo STOP-02.

Master Prompt xác định 3 role:

- ADMIN
- WAREHOUSE_KEEPER
- ACCOUNTANT

Nhưng quyền chi tiết theo `ROLE × FR × ACTION × API` chưa có nguồn baseline đủ để suy diễn an toàn.

## Gap Analysis

| Area | Status | Evidence |
|---|---|---|
| Frontend React/TypeScript/Vite | NOT STARTED | Repo trống |
| Backend FastAPI/Pydantic/SQLAlchemy | NOT STARTED | Repo trống |
| PostgreSQL | NOT STARTED | Repo trống |
| Alembic migration | NOT STARTED | Repo trống |
| Authentication | BLOCKED | Thiếu permission/business baseline |
| RBAC | BLOCKED | STOP-02 |
| Master data | BLOCKED | Thiếu Phase 1 chi tiết |
| Stock transaction | BLOCKED | Thiếu Phase 1 chi tiết |
| Reporting | BLOCKED | Thiếu baseline/test specification |
| AI FR-09 → FR-11 | PARTIAL REQUIREMENT AVAILABLE | Master Prompt có rule cấp cao nhưng thiếu traceability Phase 1 |
| Docker Compose | NOT STARTED | Repo trống |
| CI | NOT STARTED | Repo trống |
| Automated tests | NOT STARTED | Repo trống |

## Out-of-Scope Detection

Không có code hiện tại để phát hiện chức năng ngoài scope.

Các chức năng bị cấm nếu chưa được phê duyệt: đa kho, đa chi nhánh, khách hàng, bán hàng, đơn hàng, thanh toán, công nợ, vận chuyển, quản lý lô/batch/serial/hạn sử dụng, kiểm kê độc lập, tài sản, khấu hao, báo cáo tài chính và các hành động AI tự thay đổi nghiệp vụ.

## Conflict Detection

Không phát hiện conflict trong source vì repository trống.

Có một điểm cần lưu ý trong tên tài liệu: tiêu đề nhắc "quản lý nhà thuốc" nhưng Mission và Business Scope mô tả "Hệ thống Quản lý Kho tích hợp AI". Theo Master Prompt, không tự mở rộng sang nghiệp vụ bán thuốc/nhà thuốc ngoài Phase 1.

## Technical Implementation Decisions

### TID-001 — Repository structure

- Decision: dùng cấu trúc `frontend/`, `backend/`, `docs/`, `scripts/`.
- Alternatives: monorepo khác hoặc giữ cấu trúc cũ.
- Reason: repository trống; cấu trúc này khớp target architecture của Master Prompt.
- Impact: technical only, không đổi nghiệp vụ.
- Files affected: toàn repository.

### TID-002 — Backend foundation

- Decision: FastAPI + SQLAlchemy 2.x + PostgreSQL + Alembic; cấu hình bằng environment variables.
- Alternatives: framework khác.
- Reason: stack bắt buộc.
- Impact: technical only.

### TID-003 — Frontend foundation

- Decision: React + TypeScript + Vite + React Router + TanStack Query + React Hook Form + Zod + Tailwind CSS.
- Reason: stack bắt buộc.
- Impact: technical only.

## Proposed Phase 2 Sequence

1. Phase 2A foundation kỹ thuật không phụ thuộc business ambiguity.
2. Bổ sung baseline/SRS/Use Case/Test Specification vào repository.
3. Hoàn thiện Requirement Matrix và Permission Matrix.
4. Triển khai authentication/RBAC.
5. Triển khai master data.
6. Triển khai stock transaction + concurrency + cancellation + audit.
7. Reporting/export.
8. AI.
9. Hardening/CI/evidence.

## Blockers

- STOP-02 — Permission ambiguity.
- STOP-03 — Missing traceability cho UC/Business Rule/Test.
- STOP-09 — Chưa có execution evidence; không được claim VERIFIED/PASS.

Các blocker trên chỉ chặn module nghiệp vụ liên quan. Foundation kỹ thuật vẫn có thể triển khai an toàn.
