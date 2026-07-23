# Báo cáo chiến lược: chọn use case AI Agent giá trị cao nhất trên PAL

**Ngày chốt dữ liệu:** 23/07/2026  
**Đầu vào:** `report1.md`, `report2.md`  
**Đơn vị quyết định:** use case có buyer, workflow, KPI và payback—không phải chỉ là “ngành hấp dẫn”.

## Executive recommendation

Chọn **InvoiceGuard Agent: AI Agent xử lý hóa đơn và điều phối ngoại lệ trong quy trình Procure-to-Pay (P2P)** cho doanh nghiệp sản xuất–xuất khẩu quy mô vừa.

Lý do cốt lõi:

1. Giá trị gắn trực tiếp với tiền: giảm thời gian xử lý, sai thanh toán, hóa đơn trùng, bỏ sót chiết khấu và sai điều khoản.
2. PwC mô tả đúng workflow agent này và ước tính chu kỳ có thể giảm tới 80%; Deloitte ghi nhận quy trình hóa đơn truyền thống thường mất 14–16 ngày.
3. Đầu vào/đầu ra quan sát được nên demo thuyết phục hơn chatbot: invoice → PO/GRN/contract → evidence → quyết định/ngoại lệ → approval.
4. PAL phù hợp với RAG + tool calling + branching + human approval; không cần huấn luyện model riêng.
5. Có thể hoàn thành MVP bằng tài liệu và API giả lập, sau đó mở rộng sang ERP thật.

Điểm cần giữ tỉnh táo: “tới 80%” là mức tiềm năng do tư vấn công bố, không phải cam kết. Business case chính thức phải đo baseline tại khách hàng.

---

## Giai đoạn 1 — Phân tích từng báo cáo

### 1. Report 1

#### Phát hiện chính

- Profit pool tốt hình thành ở giao điểm của AI, già hóa dân số, chuyển dịch năng lượng, quy định và thương mại số xuyên biên giới.
- Đối với startup, lớp software/service quanh capex hấp dẫn hơn sở hữu hạ tầng: agentic AI, vertical SaaS, cybersecurity, regtech, payments, digital-health workflow và climate software.
- Việt Nam có lợi thế tăng trưởng, sản xuất và digital catch-up; cơ hội rõ ở B2B digitization và hệ sinh thái xuất khẩu.
- Khuyến nghị đúng về “narrow painful workflow”: export-document AI, ESG/CBAM, aquaculture traceability, clinic OS, care coordination.

#### Ngành/cụm tiềm năng

Agentic AI; vertical SaaS; cybersecurity; regtech/legaltech; payments; cross-border commerce; logistics/cold chain; digital health; energy storage; climate software; senior care; agritech/aquaculture; education/reskilling; beauty/wellness; AI-enabled BPO.

#### Số liệu đáng chú ý

- AI spend 2026 được ghi là 2,52 nghìn tỷ USD; bản Gartner mới hơn đã cập nhật thành **2,596 nghìn tỷ USD, +47% YoY**.
- Software spend 1,43 nghìn tỷ USD năm 2026.
- Kinh tế số Việt Nam 39 tỷ USD năm 2025 và khoảng 85 tỷ USD năm 2030.
- Battery storage cần tăng khoảng 14 lần lên 1.200 GW vào 2030 trong kịch bản NZE.
- Digital wallets chiếm 56% chi tiêu e-commerce toàn cầu năm 2025.

#### Xu hướng nổi bật

Agent tác vụ doanh nghiệp; AI governance; sovereign cloud; physical AI; energy storage; home-based eldercare; B2B supplier ecosystem tại Việt Nam/ASEAN; outcome-based software.

#### Điểm mạnh

- Phân biệt “market size proxy” với doanh thu thị trường.
- Phân biệt cơ hội cho startup với cơ hội cho chủ sở hữu vốn lớn.
- Nguồn nền tảng nhìn chung tốt hơn: IMF, World Bank, Gartner, IEA, WHO, OECD, McKinsey.
- Đưa ra niche cụ thể và có buyer tương đối rõ.

#### Điểm yếu

- Citation là marker nội bộ `turn...`, không thể audit từ file độc lập.
- Một số số liệu khác định nghĩa được đặt cạnh nhau (spend, revenue, GMV, capex, installed capacity).
- Ranking không có trọng số công khai; “competition intensity” càng cao hay càng thấp là tốt chưa nhất quán.
- Biên lợi nhuận là tổng hợp analyst, không phải benchmark riêng cho startup Việt Nam.
- Chưa chứng minh willingness-to-pay hoặc số lượng buyer cho từng niche.

#### Giả định chưa có căn cứ

- “Ít cạnh tranh/underexploited” dựa chủ yếu vào suy luận.
- Quy mô thị trường cha tự động chuyển thành TAM cho niche.
- Export-document AI tại Việt Nam có supply hạn chế nhưng không có competitor scan.
- Mức margin 60–85% của software được chuyển gần như trực tiếp sang sản phẩm mới, bỏ qua inference, implementation, sales và support.

**Độ tin cậy tổng thể:** **7,5/10** cho định hướng; **5,5/10** cho market sizing ở cấp niche.

### 2. Report 2

#### Phát hiện chính

- AI/agentic AI, bán dẫn, data center, BESS, cybersecurity, digital health, cold chain và AgTech là nhóm tăng trưởng.
- Vertical SaaS & Enterprise AI đứng đầu ranking tổng hợp; startup nên chọn vertical workflow và outcome-based pricing.
- Việt Nam được xem là điểm đến của sản xuất công nghệ, data center, logistics và chuyển dịch xanh.
- Đề xuất nhiều niche: legal/compliance AI, CSRD, deepfake security, hospital-at-home, smart cold chain, AI training.

#### Ngành/cụm tiềm năng

30 ngành trải từ software tới hạ tầng: AI platform, chip, cloud/data center, BESS, cyber, health, biopharma, cold chain, green logistics, AgTech, EdTech, defense, vertical SaaS, fintech, robotics, B2B commerce, pet tech, creator economy, circular economy, AgeTech, EV, consulting, DOOH, self-storage, microgrid, IP licensing, SMR, quantum, wellness tourism, smart building.

#### Số liệu đáng chú ý

- IT spend 6,15 nghìn tỷ USD năm 2026, +10,8%.
- “18 future arenas” có thể đạt 29–48 nghìn tỷ USD doanh thu năm 2040.
- AI market 539,5 tỷ USD năm 2026, CAGR 30,6%.
- Cold chain 437,5 tỷ USD năm 2026, CAGR 20,5%.
- Enterprise software 1.433,6 tỷ USD năm 2026, CAGR 14,7%.

#### Xu hướng nổi bật

Agentic AI/multi-agent; physical AI; longevity; microgrid; robotaxi; micro-credentials; automated cold chain; circular B2B; shared reality/DOOH.

#### Điểm mạnh

- Cấu trúc bao quát, viết bằng tiếng Việt, có regional view và 30 niche.
- Nhận ra đúng vertical SaaS + agent là điểm vào phù hợp với startup.
- Phân biệt một phần giữa startup/SME/nhà đầu tư chiến lược.
- “Future arenas” 29–48 nghìn tỷ USD có thể xác minh từ McKinsey.

#### Điểm yếu

- Nguồn cuối file gồm nhiều blog/SEO/market-research seller; không gắn nguồn với từng claim.
- Trộn gross margin và net margin; nhiều net margin 40–80% không hợp lý cho startup chưa đạt scale.
- Nhiều proxy sai cấp hoặc sai nhãn: microgrid dùng “$190B (bao bì/năng lượng)”; EV dùng “$540B (cấp vốn)”.
- Bảng Markdown hỏng; mục châu Âu và mục 6 bị escape; chuỗi 30 ngành thiếu heading rõ cho ngành 27.
- Ranking không được sort theo “điểm trung bình” (hạng 5/8 có 8,36 cao hơn các hạng trên).
- Claim “SaaS seat-based đang bị đào thải”, “project cancellation 50–60%”, “AI net margin 50–75%” không có bằng chứng đủ mạnh.
- Forecast World Bank 6,8% cho Việt Nam 2026 đã không còn là dự báo mới nhất được tìm thấy.

#### Giả định chưa có căn cứ

- Niche TAM và margin rất chính xác dù không có phương pháp.
- “Cạnh tranh thấp” cho nhiều lĩnh vực regulated/deep-tech.
- Thị trường tăng trưởng cao đồng nghĩa với use case phù hợp PAL.
- Tư vấn cá nhân có net margin 41% có thể mở rộng như software.
- Multi-agent end-to-end sẽ sớm sẵn sàng cho vận hành tự chủ.

**Độ tin cậy tổng thể:** **6/10** cho xu hướng lớn; **3,5/10** cho số liệu niche/margin và thứ hạng.

---

## Giai đoạn 2 — So sánh và đánh giá độ tin cậy

| Chủ đề | Report 1 | Report 2 | Phân loại | Đánh giá sau kiểm chứng |
|---|---|---|---|---|
| Vertical SaaS + agentic workflow là điểm vào tốt | Đồng ý | Đồng ý, xếp #1 | Đồng thuận | **Cao**; Gartner dự báo enterprise business apps 254B USD (2025) → 428B (2029), CAGR 13,5% |
| AI/agentic AI tăng mạnh | Đồng ý | Đồng ý | Đồng thuận | **Cao về hướng**, **trung bình về tốc độ áp dụng**; Gartner: 17% đã deploy agent, >60% dự kiến trong 2 năm |
| Chip/data center/BESS là thị trường lớn | Đồng ý nhưng kém phù hợp startup | Xếp rất cao | Đồng thuận có điều kiện | **Cao** về market tailwind, **thấp** về fit với bài build PAL |
| Việt Nam là operating base hấp dẫn | Có, nhấn mạnh export/B2B | Có, nhấn mạnh FDI/hạ tầng | Đồng thuận | **Trung bình–cao**; IMF 7,5% và World Bank 6,1% cho 2026 cho thấy cần scenario |
| Export-document/compliance AI là niche tốt | Nêu rõ | Nêu CSRD/legal compliance nhưng không export-doc rõ | Chỉ R1 | **Trung bình–cao**; pain thật, nhưng TAM/competition chưa đủ dữ liệu |
| Cold chain là cơ hội hàng đầu | Có nhưng ưu tiên software layer | Xếp #3/4 | Khác mức độ | **Trung bình**; tốt cho capital owner, không phải PAL MVP nếu chọn vận hành vật lý |
| Pet tech/creator/self-storage | Có nhưng thứ hạng vừa | Đánh giá rất cao | Chủ yếu R2 | **Thấp–trung bình** cho bài toán agent; thiếu liên hệ workflow/KPI |
| Climate/ESG compliance software | Xếp rất cao | Nêu CSRD/CBAM và consulting | Đồng thuận | **Trung bình–cao**, nhưng quy định thay đổi và cần domain expert |
| AI software margin 50–85% | Dùng gross/EBITDA có cảnh báo | Dùng nhiều “net margin” 50–75% | Mâu thuẫn định nghĩa | **Thấp** nếu dùng cho business case; phải model bottom-up |
| SaaS seat pricing bị đào thải | Không khẳng định | Khẳng định | Chỉ R2 | **Thấp**; outcome pricing tăng nhưng seat-based chưa “bị đào thải” |
| AI hoàn toàn tự chủ | Thận trọng hơn | Kỳ vọng multi-agent end-to-end | Mâu thuẫn | **Thấp** ở hiện tại; Gartner nói fully autonomous chưa sẵn sàng cho đa số use case |

### Kết luận so sánh

Phần giao nhau đáng tin nhất là: **vertical workflow software + agent + compliance/operations**. Phần không nên dùng để chọn bài là thứ hạng thị trường rộng, net margin cực cao và “explosive trend” chưa gắn buyer. Báo cáo 1 là nền tốt hơn cho framing; báo cáo 2 hữu ích như idea inventory, không nên dùng như nguồn số liệu duy nhất.

---

## Giai đoạn 3 — Nghiên cứu bổ sung và hiệu chỉnh

1. **AI spend:** Gartner tháng 5/2026 dự báo 2,596 nghìn tỷ USD, +47% YoY; hạ tầng chiếm hơn 45%. Điều này sửa số 2,52 nghìn tỷ trong R1 và chống lại suy luận “toàn bộ là ngân sách phần mềm agent”.
2. **Adoption reality:** Gartner 2026 cho biết chỉ 17% tổ chức đã deploy AI agent, dù hơn 60% dự kiến trong hai năm. Phần lớn deployment còn hẹp; fully autonomous agent chưa phù hợp đa số use case.
3. **Enterprise apps:** Gartner ước 254B USD năm 2025 và 428B USD năm 2029, CAGR 13,5%. Đây là proxy tốt hơn cho use case workflow so với tổng AI spend.
4. **Finance-agent evidence:** PwC nêu invoice extraction + PO/contract matching có thể giảm cycle time tới 80% và cải thiện audit trail.
5. **Procurement value:** McKinsey ước AI ở quy mô lớn có thể giảm 5–15% procurement spend qua compliance/data-driven decision; 50–80% efficiency ở một số hoạt động và 5–10% procurement operating cost. Đây là potential range, không phải guaranteed ROI.
6. **Baseline hóa đơn:** Deloitte benchmark quy trình truyền thống mất 14–16 ngày trước khi chuẩn bị thanh toán.
7. **Việt Nam:** IMF tháng 7/2026 là 7,5%; World Bank tháng 9/2025 là 6,1% cho 2026. Khác biệt do vintage và mô hình; không nên chọn một số duy nhất làm “sự thật”.
8. **E-invoice:** Nghị định 70/2025/NĐ-CP có hiệu lực 1/6/2025, mở rộng/làm rõ hóa đơn điện tử; World Bank ghi nhận tới 31/3/2023 toàn bộ VAT taxpayers gồm hơn 851.000 doanh nghiệp và 65.000 hộ kinh doanh đã thuộc hệ thống e-invoice. Đây là hạ tầng dữ liệu thuận lợi cho invoice agent.
9. **SME adoption:** Nghiên cứu World Bank tại Việt Nam cảnh báo adoption suy yếu khi lợi ích không tức thời/tangible. Do đó pilot phải báo cáo hours, exceptions và money recovered ngay tuần đầu.

---

## Giai đoạn 4 — Top 20 cơ hội kinh doanh

### Cách chấm

Mọi điểm đều theo chiều **10 = hấp dẫn hơn**:

- Size (10%), CAGR/growth (8%), cạnh tranh thấp (5%), margin (10%).
- tự động hóa (12%), AI applicability (15%), PAL-agent fit (18%).
- dễ triển khai (8%), chi phí thấp (6%), payback nhanh (8%).

“Quy mô/CAGR” là **parent-market proxy**, không phải TAM đã audit của niche. H = nguồn chính thống/primary hoặc consultancy mạnh; M = proxy hợp lý; L = commercial estimate/claim chưa đủ kiểm chứng.

| # | Cơ hội AI Agent | Market proxy; CAGR/signal; confidence | Size | CAGR | Cạnh tranh thấp | Margin | Auto | AI | PAL | Dễ | Chi phí thấp | Payback | Điểm |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Invoice-to-Pay exception & contract-compliance | Enterprise apps 254B→428B USD, 2025–29; 13,5%; H | 9 | 9 | 6 | 9 | 10 | 10 | 10 | 9 | 9 | 10 | **9,38** |
| 2 | Export-document & trade-compliance | E-commerce 4T (2022)→14–20T (2040); ~7–9%; M | 10 | 8 | 8 | 9 | 9 | 10 | 10 | 8 | 9 | 9 | **9,22** |
| 3 | RFP/tender qualification & response | Enterprise apps proxy; 13,5%; M | 8 | 9 | 6 | 9 | 9 | 10 | 10 | 10 | 10 | 9 | **9,22** |
| 4 | Customer-support resolution agent B2B | AI software 453B USD 2026; +60% YoY; H | 10 | 10 | 3 | 8 | 10 | 10 | 9 | 9 | 9 | 9 | **9,05** |
| 5 | Procurement contract leakage & supplier-risk | Enterprise apps 254B→428B; 13,5%; H | 9 | 9 | 6 | 9 | 9 | 10 | 10 | 8 | 8 | 9 | **9,04** |
| 6 | Sales lead-to-proposal agent | Enterprise apps proxy; 13,5%; M | 9 | 9 | 4 | 9 | 9 | 10 | 9 | 9 | 9 | 8 | **8,82** |
| 7 | HR onboarding & policy agent | Enterprise apps proxy; 13,5%; M | 8 | 9 | 4 | 8 | 9 | 9 | 9 | 10 | 10 | 9 | **8,69** |
| 8 | Legal contract review & obligation tracking | Enterprise apps proxy; 13,5%; M | 8 | 9 | 5 | 9 | 8 | 10 | 9 | 8 | 8 | 8 | **8,51** |
| 9 | KYC/AML alert investigation | AI cyber 51,3B USD 2026; 98% YoY; H | 8 | 10 | 5 | 9 | 9 | 10 | 9 | 6 | 6 | 8 | **8,43** |
| 10 | Logistics shipment-exception control tower | E-commerce arena proxy; 7–9%; M | 10 | 8 | 6 | 8 | 9 | 9 | 9 | 7 | 7 | 8 | **8,41** |
| 11 | E-commerce returns/chargeback agent | E-commerce 4T→14–20T; ~7–9%; M | 10 | 8 | 5 | 7 | 9 | 9 | 9 | 8 | 8 | 8 | **8,40** |
| 12 | ESG/CBAM evidence & reporting | Adjacent energy-transition spend 2T+; regulation-led; M | 9 | 8 | 7 | 9 | 8 | 9 | 9 | 6 | 7 | 8 | **8,26** |
| 13 | AI tutor for job-linked upskilling | Education parent market large; R2 13,5–16,2%; L | 8 | 8 | 3 | 8 | 9 | 9 | 9 | 9 | 9 | 7 | **8,26** |
| 14 | Cybersecurity incident triage | AI cyber 51,3B→86,0B, 2026–27; 67%; H | 8 | 10 | 4 | 9 | 9 | 10 | 8 | 6 | 6 | 8 | **8,20** |
| 15 | Manufacturing quality/CAPA investigation | Enterprise apps proxy; 13,5%; M | 8 | 9 | 7 | 9 | 8 | 9 | 9 | 6 | 6 | 8 | **8,18** |
| 16 | Field-service maintenance coordinator | Robotics/service ecosystem; installations +9%; M | 8 | 8 | 6 | 8 | 8 | 9 | 8 | 6 | 6 | 7 | **7,69** |
| 17 | Healthcare admin/care-navigation | 129 countries có digital-health strategy; policy signal; H | 8 | 8 | 6 | 8 | 8 | 9 | 8 | 5 | 5 | 7 | **7,55** |
| 18 | Aquaculture traceability/export agent | FAO aquaculture target +35% by 2030; M | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 6 | 7 | 7 | **7,48** |
| 19 | Senior-care coordination agent | Demographic/policy signal; no clean niche TAM; M | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 6 | 6 | 7 | **7,42** |
| 20 | Energy-storage O&M anomaly coordinator | Storage 1.200 GW by 2030; ~25% deployment CAGR; H | 9 | 10 | 7 | 8 | 7 | 8 | 7 | 4 | 4 | 6 | **7,19** |

### Đọc bảng đúng cách

- Điểm là công cụ ra quyết định cho **bài PAL**, không phải khuyến nghị đầu tư tài chính.
- RFP và customer support có điểm rất cao nhưng bị điều chỉnh trong judgment vì direct value capture thấp hơn hoặc cạnh tranh mạnh hơn.
- Hạng 1–5 được chọn bằng cả score và “strategic judgment overlay”: evidence, buyer urgency, demo clarity, defensibility.

---

## Giai đoạn 5 — Top 5 use case

### 1. InvoiceGuard — Invoice-to-Pay exception agent

- **Business problem:** AP mất thời gian đọc, nhập, match và truy đuổi ngoại lệ; lỗi làm chậm thanh toán và rò rỉ giá trị.
- **Pain point:** nhiều định dạng; PO/GRN/contract rời rạc; hóa đơn trùng; thay đổi bank detail; email qua lại.
- **Target:** CFO, AP Manager, Procurement Manager tại doanh nghiệp sản xuất–xuất khẩu 100–2.000 nhân sự.
- **Existing workflow:** email/upload → nhập tay → tìm PO/GRN → đối soát → hỏi vendor → approval → ERP.
- **AI opportunity:** document understanding, retrieval, deterministic matching, exception reasoning, drafting và routing.
- **Impact:** cycle time, touchless rate, exception aging, duplicate prevented, discount captured.
- **ROI minh họa:** 90% năm 1; payback ~6,3 tháng với 20.000 invoice/năm và các giả định trong file ROI.
- **Vì sao nổi bật:** direct cash + workflow rõ + evidence mạnh + demo an toàn.

### 2. ExportFlow — Export-document & trade-compliance agent

- **Problem/pain:** dữ liệu không nhất quán giữa PO, invoice, packing list, shipping instruction, certificate; sửa lỗi gây delay.
- **Target:** exporter Việt Nam, freight forwarder, 3PL.
- **Workflow:** nhân viên copy dữ liệu qua template, tra checklist, gửi nhiều bên, sửa chứng từ.
- **AI:** extract/reconcile fields, checklist theo lane/customer, draft missing docs và correction email.
- **Impact:** giảm document-prep time, discrepancy, shipment delay.
- **ROI ước tính:** 40–120%/năm tùy volume; cần pilot để xác nhận cost-of-error.
- **Nổi bật:** Việt Nam-specific, ít generic hơn AP, demo trực quan.
- **Điểm trừ:** cần knowledge pháp lý/thương mại cập nhật; lỗi có thể giữ hàng.

### 3. ProcureWatch — Contract leakage & supplier-risk agent

- **Problem:** discount/rebate/tier price và SLA trong hợp đồng không được áp dụng xuyên suốt.
- **Target:** procurement/finance của doanh nghiệp có spend lớn.
- **Workflow:** sample audit thủ công, theo dõi spreadsheet.
- **AI:** đọc nghĩa vụ, monitor invoice/PO theo thời gian, phát hiện cumulative threshold và soạn claim.
- **Impact:** spend recovered, compliance rate, audit coverage.
- **ROI ước tính:** rất cao nếu recover chỉ 0,1–0,5% addressable spend.
- **Nổi bật:** economic value lớn và data moat.
- **Điểm trừ:** contract interpretation khó; cần lịch sử giao dịch và legal review.

### 4. BidPilot — RFP/tender qualification & response agent

- **Problem:** đội sales/solution tốn nhiều ngày đọc RFP và gom bằng chứng.
- **Target:** B2B software, system integrator, construction/engineering.
- **Workflow:** đọc PDF → compliance matrix → assign owners → tìm case study → draft.
- **AI:** requirement extraction, bid/no-bid score, evidence-grounded answer, gap tracking.
- **Impact:** response time, win-rate, proposal capacity.
- **ROI ước tính:** 50–200% nếu tăng thêm một win/năm; biến động cao.
- **Nổi bật:** MVP nhanh nhất và demo đẹp.
- **Điểm trừ:** attribution ROI khó; hallucinated claim tạo rủi ro hợp đồng.

### 5. ResolveAI — B2B customer-support resolution agent

- **Problem:** ticket lặp lại, agent tìm knowledge và thao tác nhiều hệ thống.
- **Target:** SaaS/e-commerce/fintech support.
- **Workflow:** classify → search → troubleshoot → refund/escalate → update CRM.
- **AI:** intent, RAG, tool execution, summary và routing.
- **Impact:** first-contact resolution, handle time, cost/ticket, CSAT.
- **ROI ước tính:** 30–100% tùy ticket deflection.
- **Nổi bật:** dễ triển khai và dữ liệu volume lớn.
- **Điểm trừ:** thị trường đông; dễ trở thành chatbot không khác biệt.

---

## Giai đoạn 6 — Quyết định cuối

### Chọn InvoiceGuard

| Tiêu chí | Đánh giá |
|---|---|
| Business value | Trực tiếp bảo vệ cash, working capital, compliance và năng suất |
| Demo | Ba tình huống tạo “aha”: straight-through, price mismatch, bank-change fraud |
| Complexity | Vừa phải; MVP dùng PDF/CSV/JSON + mock tools |
| Scalability | Invoice → AP → procurement compliance → AR/collections → treasury |
| Tính mới | Không mới ở OCR; mới ở evidence-grounded exception orchestration và local policy |
| Tính thực tế | Quyết định được neo bằng PO/GRN/contract và rule; người phê duyệt giữ quyền |
| ROI | Baseline dễ đo; conservative model cho payback khoảng 6 tháng |

### Vì sao không chọn bốn use case còn lại

- **ExportFlow:** khác biệt hơn nhưng cần corpus quy định, HS/origin expertise và liability cao hơn; phù hợp phase 2 sau khi chứng minh pattern document-reconciliation.
- **ProcureWatch:** value có thể lớn hơn nhưng cần hợp đồng dài, dữ liệu lịch sử và xử lý nghĩa vụ phức tạp; khó hoàn thiện demo đáng tin trong thời gian ngắn.
- **BidPilot:** demo nhanh nhưng giá trị tài chính phụ thuộc win-rate, khó chứng minh causality và cạnh tranh sản phẩm cao.
- **ResolveAI:** triển khai dễ nhưng rất crowded; nguy cơ bài nộp trông như chatbot/RAG thông thường.

### Điều kiện go/no-go sau pilot

Go nếu trong 4 tuần đạt: ≥60% field extraction đúng không cần sửa; ≥90% match accuracy trên test set đã gán nhãn; giảm ≥40% manual minutes/invoice; zero unauthorized posting; ≥70% người dùng đánh giá explanation hữu ích. Nếu không đạt, thu hẹp vào một vendor group hoặc một loại invoice thay vì tăng autonomy.
