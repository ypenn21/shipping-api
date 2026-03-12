# Feature Implementation Plan: OpenAPI Spec for Shipping CRUD REST APIs

> **Jira Ticket:** [OPS-9](https://google-team-coler8gf.atlassian.net/browse/OPS-9) — *Create an OpenAPI spec for backend CRUD REST APIs* (Medium, To Do)

## 📋 Todo Checklist
- [x] Create the OpenAPI 3.0 spec YAML file at `api/openapi.yaml`
- [x] Define all 7 endpoints (discovery, liveness, readiness, CRUD packages)
- [x] Define all request/response schemas matching the `Package` data model
- [x] Cross-validate against `main.py` routes and `curl.sh` test payloads
- [x] Final review and manual verification

## 🔍 Analysis & Investigation

### Codebase Structure
| File | Purpose |
|---|---|
| `main.py` | Flask app with 7 route handlers |
| `data_model.py` | SQLAlchemy `Package` model (7 columns) |
| `connect_connector.py` | In-memory SQLite engine + session factory |
| `curl.sh` | Integration test script showing request/response shapes |
| `tests/test.py` | Minimal unittest scaffold |

### API Endpoints Discovered

| Method | Path | Handler | Description |
|---|---|---|---|
| `GET` | `/discovery` | `discovery()` | Returns service metadata (name, version, owners, team, org) |
| `GET` | `/liveness` | `liveness()` | Health check — returns status, code, timestamp |
| `GET` | `/readiness` | `readiness()` | Readiness check — returns status, code, timestamp |
| `POST` | `/packages` | `create_package()` | Create a new package. Body: JSON with `product_id`, `height`, `width`, `depth`, `weight`, `special_handling_instructions`. Returns `{ package_id }` with `201`. |
| `GET` | `/packages/{product_id}` | `get_package(product_id)` | Get package by `product_id` (int path param). Returns package details or `404`. |
| `PUT` | `/packages/{package_id}` | `update_package(package_id)` | Update package by `id` (int path param). Partial update supported. Returns updated package or `404`. |
| `DELETE` | `/packages/{package_id}` | `delete_package(package_id)` | Delete package by `id` (int path param). Returns `204` on success or `404`. |

### Package Data Model
From `data_model.py`:
- `id` — Integer, primary key, autoincrement
- `product_id` — String, not nullable
- `height` — Float
- `width` — Float
- `depth` — Float
- `weight` — Float
- `special_handling_instructions` — String (nullable)

### Key Observations
- **GET vs PUT/DELETE use different ID semantics**: `GET /packages/{product_id}` filters by `product_id` (string column, but path param is `int`), while `PUT` and `DELETE /packages/{package_id}` filter by `id` (primary key).
- **No response envelope on errors**: Flask's `abort()` returns standard HTML error pages, not JSON. The spec should document what the API *intends* to return.
- **`special_handling_instructions`** is optional on create (no `abort` if missing).
- The Jira ticket explicitly says: *"Just create an OpenAPI spec YAML file. Don't add any dependencies or try to host the OpenAPI spec."*

## 📝 Implementation Plan

### Prerequisites
None — this is a documentation-only change. No new dependencies required.

### Step-by-Step Implementation

1. **Create `api/openapi.yaml`** — a single OpenAPI 3.0.3 specification file
   - File to create: `api/openapi.yaml`
   - Define `openapi`, `info` (title: "Shipping Service API", version: "1.0.0"), and `servers` blocks
   - Define all 7 paths with their methods, parameters, request bodies, and responses
   - Define reusable `components/schemas` for: `Package`, `PackageCreate`, `PackageUpdate`, `DiscoveryResponse`, `HealthResponse`, `ErrorResponse`
   - Map every field type to its OpenAPI equivalent (`Float` → `number`, `String` → `string`, `Integer` → `integer`)

2. **Cross-validate** the spec against:
   - `main.py` route definitions (methods, paths, status codes)
   - `curl.sh` request payloads (field names, types)
   - `data_model.py` column definitions (types, nullable)

### Testing Strategy

Since this is a YAML file with no runtime dependencies, verification is:

1. **Lint the YAML** — run `python3 -c "import yaml; yaml.safe_load(open('api/openapi.yaml'))"` to confirm it's valid YAML
2. **Manual Review** — visually inspect that every endpoint in `main.py` has a corresponding path in the spec, and every schema field matches `data_model.py`

## 🎯 Success Criteria
- A single `api/openapi.yaml` file exists with valid OpenAPI 3.0.3 syntax
- All 7 endpoints are documented with correct methods, paths, parameters, request/response schemas, and status codes
- No new dependencies are added
- The spec is not hosted or served — it's a standalone documentation file
