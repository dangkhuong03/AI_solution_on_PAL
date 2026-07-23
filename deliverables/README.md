# Bộ bài nộp: AI solution on PAL

**Khuyến nghị cuối cùng:** xây dựng **InvoiceGuard Agent — AI Agent xử lý hóa đơn, đối soát PO/biên nhận/hợp đồng và điều phối ngoại lệ cho doanh nghiệp sản xuất–xuất khẩu**.

InvoiceGuard không tự thanh toán. Agent đọc hóa đơn, lấy dữ liệu liên quan, kiểm tra 3-way match và điều khoản hợp đồng, phát hiện trùng lặp/thay đổi tài khoản ngân hàng, giải thích sai lệch, soạn yêu cầu làm rõ và chuyển đúng người phê duyệt. Mọi hành động tài chính vẫn có human-in-the-loop và audit trail.

## Cấu trúc

- [01_strategy_report.md](01_strategy_report.md): phân tích hai báo cáo, kiểm chứng, bảng so sánh, Top 20, Top 5 và quyết định cuối.
- [02_pal_solution_blueprint.md](02_pal_solution_blueprint.md): thiết kế workflow, kiến trúc, dữ liệu, tools, prompt, guardrails và KPI.
- [03_submission_pack.md](03_submission_pack.md): one-pager, checklist build, demo script 5–10 phút và pitch 3–5 phút.
- [04_evidence_and_roi.md](04_evidence_and_roi.md): sổ đăng ký bằng chứng, giả định, công thức ROI và giới hạn nghiên cứu.
- [05_jury_reassessment.md](05_jury_reassessment.md): phản biện độc lập theo góc nhìn giám khảo; so sánh 11 use case và đề xuất ProcurePilot thay InvoiceGuard.

## Cập nhật sau phản biện của hội đồng

Nếu tối ưu cho **execution certainty**, InvoiceGuard vẫn là lựa chọn an toàn. Nếu tối ưu cho **xác suất thắng cuộc thi**, hội đồng xếp **ProcurePilot — RFQ-to-Award Procurement Agent** cao hơn vì thể hiện planning, reasoning, multi-tool orchestration và business impact rõ hơn. Xem scorecard và điều kiện quyết định trong tài liệu phản biện.

## Kết luận điều hành

Hai báo cáo cùng đúng ở cấp độ chiến lược: cơ hội tốt nhất cho một đội nhỏ không nằm ở việc xây hạ tầng AI, chip hay kho lạnh, mà ở **lớp phần mềm workflow dọc**, giải quyết một ma sát có chi phí rõ ràng. Tuy nhiên, cả hai đều đi từ “thị trường lớn” đến “cơ hội startup” quá nhanh; nhiều TAM, CAGR và biên lợi nhuận không cùng định nghĩa hoặc không truy xuất được nguồn.

Sau khi chuẩn hóa về use case và chấm theo ưu tiên của đề bài, InvoiceGuard đứng đầu vì có buyer rõ (CFO/AP/Procurement), dữ liệu demo dễ tạo, quyết định phần lớn có thể kiểm tra bằng quy tắc, tác động trực tiếp đến thời gian chu trình và value leakage, triển khai MVP nhanh, và có đường mở rộng từ một agent thành Finance Operations platform.

> **Phạm vi PAL:** chưa có tài liệu đặc tả PAL trong workspace. Bộ thiết kế dùng tập năng lực tối thiểu thường có của một agent builder: instructions, knowledge base/RAG, structured output, tools/API, workflow/branching, human approval và logs. Tên node cần được ánh xạ sang UI/API cụ thể của PAL khi triển khai.
