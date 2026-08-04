# Awesome-Semantic-Layer-Platform

# Similar Projects to Semantic Layer Platforms

**Semantic Layer Platforms** provide a consistent, governed layer of business metrics and definitions on top of data warehouses. They enable a single source of truth for metrics that can be consumed by BI tools, embedded analytics, AI agents, and applications via SQL, APIs, or other interfaces. Leading platforms and approaches include dbt Cloud MetricFlow / dbt Semantic Layer, AtScale, Cube, Honeydew, Transform, Omni, GoodData Semantic Layer, Looker Semantic Model (LookML), Power BI Semantic Models, Metric Insights, Kyvos, and Hex Metrics.

Below is a **curated list** of notable platforms and their open-source equivalents. The semantic layer space has strong open-source foundations, particularly around metrics definition and headless BI.

## 🏢 SaaS / Hosted Platforms

- **[dbt Semantic Layer / MetricFlow](https://www.getdbt.com/product/semantic-layer)** — Metrics defined in dbt projects and served through dbt Cloud (MetricFlow is the open-source engine).
- **[Cube](https://cube.dev/)** — Popular headless BI and semantic layer platform with strong API, caching, and embedded analytics capabilities (open-source core available).
- **[AtScale](https://www.atscale.com/)** — Enterprise semantic / virtual OLAP layer with broad BI tool compatibility (MDX/DAX/SQL).
- **[Honeydew](https://honeydew.ai/)**, **[Transform](https://transform.co/)**, **[Omni](https://omni.co/)**, **[GoodData](https://www.gooddata.com/)** — Modern semantic modeling and metrics platforms.
- **Looker (LookML)**, **Power BI Semantic Models**, **Metric Insights**, **Kyvos**, **Hex Metrics** — Platform-native or specialized semantic modeling approaches inside major BI and analytics tools.

## 🔓 Open-Source Software

### Core Open-Source Semantic / Metrics Layers
- **[Cube Core](https://github.com/cube-js/cube)** — The leading open-source (Apache 2.0) semantic layer and headless BI platform. Define metrics in YAML/JavaScript, serve them via SQL, REST, GraphQL, and more, with built-in caching and pre-aggregations. Fully self-hostable.
- **[MetricFlow](https://github.com/dbt-labs/metricflow)** — Open-source metrics engine developed by dbt Labs. Powers the dbt Semantic Layer and allows defining reusable metrics in YAML that compile to efficient SQL.
- **[Lightdash](https://github.com/lightdash/lightdash)** — Open-source BI tool that turns dbt models and metrics into a governed exploration experience. Excellent companion when you want an open-source consumption layer on top of dbt + MetricFlow.
- Emerging universal metrics runtimes (such as Sidemantic) that aim to import and serve models from multiple formats (Cube, MetricFlow, LookML, etc.).

### Related Open-Source Projects
- **Malloy** — Open-source experimental language for describing data relationships and nested queries (useful in semantic modeling contexts).
- Open-source BI platforms (Apache Superset, Metabase, etc.) that can consume well-modeled data and, in some cases, integrate with metrics layers.
- Community tools for converting or managing semantic models across formats as the Open Semantic Interchange (OSI) ecosystem matures.

### Typical Open-Source Approach
1. **Transformations & base models** — dbt Core
2. **Metrics definitions** — MetricFlow or Cube data models
3. **Serving layer** — Cube Core (APIs + caching) or direct warehouse access
4. **Exploration / BI** — Lightdash, Superset, or Metabase
5. **Governance** — Git-based versioning of YAML/SQL models + warehouse access controls

This stack delivers a fully open, self-hosted semantic layer with consistent metrics, API access, and the flexibility to evolve definitions alongside your data models—without per-seat semantic layer licensing.

---

**How to contribute**  
Fork this repository, add a new project (with link + short description + category), and open a pull request.  
Prefer actively maintained open-source projects related to semantic layers, metrics layers, headless BI, or governed metrics definition.

**License**  
This list is public domain / CC0. Feel free to copy into your own awesome list or README.

Star the projects you find useful — open semantic layers help teams trust their metrics across every tool! 📊
