# Production checklist

- [ ] Thay static bearer token bằng OAuth/JWT hoặc identity provider.
- [ ] Không lưu secret trong source hoặc registry JSON.
- [ ] Dùng structured logging và request ID.
- [ ] Thêm timeout, retry có giới hạn và circuit breaker cho WeatherAPI.
- [ ] Có health/readiness endpoint và monitoring.
- [ ] Giữ tool cũ khi thay đổi schema; đánh dấu deprecated trước khi xóa.
- [ ] Pin dependency và cập nhật lockfile định kỳ.
- [ ] Viết unit/integration test cho từng tool và transport.
- [ ] Giới hạn CORS, network access và quyền của từng client.
