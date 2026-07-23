# Bộ bài nộp: AI solution on PAL

**Use case đã chốt:** xây dựng **ProcurePilot — AI Procurement Decision Agent for RFQ-to-Award**.

ProcurePilot phân tích Purchase Request, supplier master/performance, báo giá và rủi ro; lập sourcing plan; chuẩn hóa quote; tính landed TCO; chạy award scenarios; và chuẩn bị recommendation/PO draft. Agent không tự gửi RFQ, award supplier hoặc release PO. Mọi hành động ràng buộc đều có human-in-the-loop và audit trail.

## Cấu trúc

- [01_strategy_report.md](01_strategy_report.md): phân tích hai báo cáo, kiểm chứng, bảng so sánh, Top 20, Top 5 và quyết định cuối.
- [02_pal_solution_blueprint.md](02_pal_solution_blueprint.md): thiết kế workflow, kiến trúc, dữ liệu, tools, prompt, guardrails và KPI.
- [03_submission_pack.md](03_submission_pack.md): one-pager, checklist build, demo script 5–10 phút và pitch 3–5 phút.
- [04_evidence_and_roi.md](04_evidence_and_roi.md): sổ đăng ký bằng chứng, giả định, công thức ROI và giới hạn nghiên cứu.
- [05_jury_reassessment.md](05_jury_reassessment.md): phản biện độc lập theo góc nhìn giám khảo; so sánh 11 use case và đề xuất ProcurePilot thay InvoiceGuard.
- [06_procurepilot_pal_blueprint.md](06_procurepilot_pal_blueprint.md): kiến trúc enterprise đầy đủ cho ProcurePilot trên PAL.
- [07_procurepilot_demo_and_pitch.md](07_procurepilot_demo_and_pitch.md): one-pager, demo 7 phút, pitch 3–5 phút và build checklist.
- [08_procurepilot_pal_mvp_blueprint.md](08_procurepilot_pal_mvp_blueprint.md): blueprint triển khai chính cho challenge—một PAL Agent, sáu built-in capabilities, không enterprise integration.
- [09_procurepilot_source_audit_bugfix.md](09_procurepilot_source_audit_bugfix.md): audit bốn lỗi live test, root cause, file fixes và prompt blocks copy-ready.

## Blueprint triển khai hiện hành

Sử dụng `08_procurepilot_pal_mvp_blueprint.md` để build challenge. `06_procurepilot_pal_blueprint.md` là kiến trúc enterprise dài hạn và chỉ dùng cho phần roadmap/Q&A, không dùng làm build specification.

## Cập nhật sau phản biện của hội đồng

Nếu tối ưu cho **execution certainty**, InvoiceGuard vẫn là lựa chọn an toàn. Nếu tối ưu cho **xác suất thắng cuộc thi**, hội đồng xếp **ProcurePilot — RFQ-to-Award Procurement Agent** cao hơn vì thể hiện planning, reasoning, multi-tool orchestration và business impact rõ hơn. Xem scorecard và điều kiện quyết định trong tài liệu phản biện.

## Kết luận điều hành

Hai báo cáo cùng đúng ở cấp độ chiến lược: cơ hội tốt nhất cho một đội nhỏ không nằm ở việc xây hạ tầng AI, chip hay kho lạnh, mà ở **lớp phần mềm workflow dọc**, giải quyết một ma sát có chi phí rõ ràng. Tuy nhiên, cả hai đều đi từ “thị trường lớn” đến “cơ hội startup” quá nhanh; nhiều TAM, CAGR và biên lợi nhuận không cùng định nghĩa hoặc không truy xuất được nguồn.

Sau vòng phản biện theo tiêu chí cuộc thi, ProcurePilot được chọn vì có buyer rõ, tác động trực tiếp tới spend/cycle time/risk, thể hiện được planning–reasoning–tool use trong demo, vẫn có thể kiểm soát bằng deterministic scoring và human approval, đồng thời mở rộng tự nhiên từ sourcing sang supplier risk, contract compliance và downstream invoice matching.

> **Phạm vi PAL:** chưa có tài liệu đặc tả PAL trong workspace. Bộ thiết kế dùng tập năng lực tối thiểu thường có của một agent builder: instructions, knowledge base/RAG, structured output, tools/API, workflow/branching, human approval và logs. Tên node cần được ánh xạ sang UI/API cụ thể của PAL khi triển khai.
