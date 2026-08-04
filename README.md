![Awesome Semantic Layer](assets/banner.svg)

<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

# Awesome Semantic Layer Platform: A Curated List of Headless BI and Metrics Layers

## 🔍 Similar Projects to Semantic Layer Platforms

**Semantic Layer Platforms** provide a consistent, governed layer of business metrics and definitions on top of data warehouses. They enable a single source of truth for metrics that can be consumed by BI tools, embedded analytics, AI agents, and applications via SQL, APIs, or other interfaces. Leading platforms and approaches include dbt Cloud MetricFlow / dbt Semantic Layer, AtScale, Cube, Honeydew, Transform, Omni, GoodData Semantic Layer, Looker Semantic Model (LookML), Power BI Semantic Models, Metric Insights, Kyvos, and Hex Metrics.

Below is a **curated list** of notable platforms and their open-source equivalents. The semantic layer space has strong open-source foundations, particularly around metrics definition and headless BI.

## 🏢 SaaS / Hosted Platforms

| Platform | Description | Pricing / Free Tier Limit | Company Size / Valuation |
| :--- | :--- | :--- | :--- |
| **Power BI Semantic Models** | Platform-native semantic modeling inside major BI and analytics tools. | Power BI Desktop is free; Pro starts at $10/user/mo. | ~$3T (Microsoft) |
| **Looker (LookML)** | Platform-native semantic modeling inside major BI and analytics tools. | Enterprise pricing (Contact Sales). | ~$2T (Google) |
| **[dbt Semantic Layer / MetricFlow](https://www.getdbt.com/product/semantic-layer)** | Metrics defined in dbt projects and served through dbt Cloud. | Free Developer tier (1 developer seat, 1 project); Paid starts at $100/mo. | ~$4.2B |
| **[Transform](https://transform.co/)** | Modern semantic modeling and metrics platform. | N/A (Acquired by dbt Labs). | ~$4.2B (dbt) |
| **[Cube](https://cube.dev/)** | Headless BI and semantic layer platform with strong API, caching, embedded analytics. | Free Developer tier (1 deployment, up to 1GB data passed); Paid starts at $99/mo. | ~$500M |
| **[AtScale](https://www.atscale.com/)** | Enterprise semantic / virtual OLAP layer with broad BI tool compatibility. | Enterprise pricing (Contact Sales). No free tier. | ~$500M |
| **[Hex Metrics](https://hex.tech)** | Platform-native semantic modeling inside major BI and analytics tools. | Community tier is free (up to 3 projects, 5 authors); Paid starts at $36/user/mo. | ~$300M |
| **[GoodData](https://www.gooddata.com/)** | Modern semantic modeling and metrics platform. | Free tier available (up to 5 workspaces); Paid starts at $1,500/mo. | ~$300M |
| **[Omni](https://omni.co/)** | Modern semantic modeling and metrics platform. | Custom pricing (Contact Sales). | ~$100M |
| **Kyvos** | Platform-native semantic modeling inside major BI and analytics tools. | Custom pricing (Contact Sales). | ~$50M |
| **Metric Insights** | Platform-native semantic modeling inside major BI and analytics tools. | Custom pricing (Contact Sales). | ~$50M |
| **[Honeydew](https://honeydew.ai/)** | Modern semantic modeling and metrics platform. | Custom pricing (Contact Sales). | ~$10M |

## 🔓 Open-Source Software

### 🛠️ Core Open-Source Semantic / Metrics Layers
- **[Apache Superset](https://github.com/apache/superset)** [![GitHub stars](https://img.shields.io/github/stars/apache/superset?style=social&color=white)](https://github.com/apache/superset/stargazers) — Modern, enterprise-ready business intelligence web application.
- **[Metabase](https://github.com/metabase/metabase)** [![GitHub stars](https://img.shields.io/github/stars/metabase/metabase?style=social&color=white)](https://github.com/metabase/metabase/stargazers) — The simplest, fastest way to get BI and analytics to everyone in your company.
- **[Hasura](https://github.com/hasura/graphql-engine)** [![GitHub stars](https://img.shields.io/github/stars/hasura/graphql-engine?style=social&color=white)](https://github.com/hasura/graphql-engine/stargazers) — Blazing fast, instant realtime GraphQL APIs on your DB with fine grained access control.
- **[Cube Core](https://github.com/cube-js/cube)** [![GitHub stars](https://img.shields.io/github/stars/cube-js/cube?style=social&color=white)](https://github.com/cube-js/cube/stargazers) — The leading open-source (Apache 2.0) semantic layer and headless BI platform. Define metrics in YAML/JavaScript, serve them via SQL, REST, GraphQL, and more, with built-in caching and pre-aggregations. Fully self-hostable.
- **[Rill](https://github.com/rilldata/rill)** [![GitHub stars](https://img.shields.io/github/stars/rilldata/rill?style=social&color=white)](https://github.com/rilldata/rill/stargazers) — Developer-first analytical tool that makes it easy to build dashboards from datasets.
- **[Evidence](https://github.com/evidence-dev/evidence)** [![GitHub stars](https://img.shields.io/github/stars/evidence-dev/evidence?style=social&color=white)](https://github.com/evidence-dev/evidence/stargazers) — Business intelligence as code. Build reports using SQL and Markdown.
- **[Lightdash](https://github.com/lightdash/lightdash)** [![GitHub stars](https://img.shields.io/github/stars/lightdash/lightdash?style=social&color=white)](https://github.com/lightdash/lightdash/stargazers) — Open-source BI tool that turns dbt models and metrics into a governed exploration experience. Excellent companion when you want an open-source consumption layer on top of dbt + MetricFlow.
- **[MetricFlow](https://github.com/dbt-labs/metricflow)** [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/metricflow?style=social&color=white)](https://github.com/dbt-labs/metricflow/stargazers) — Open-source metrics engine developed by dbt Labs. Powers the dbt Semantic Layer and allows defining reusable metrics in YAML that compile to efficient SQL.
- Emerging universal metrics runtimes (such as Sidemantic) that aim to import and serve models from multiple formats (Cube, MetricFlow, LookML, etc.).

### 🔗 Related Open-Source Projects
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

## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Semantic-Layer-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
