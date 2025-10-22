# Workshop Module: Maestro Validated Output (MVO)

## What is Validated Output?

Validated Output ensures LLMs consistently follow complex instructions with multiple constraints. Instead of hoping your prompt works, Maestro uses computational resources to validate and automatically fix outputs until they meet your requirements.

**The core problem**: Even advanced LLMs fail to satisfy all requirements in complex prompts. You get no visibility into what failed, leading to manual trial-and-error.

**Maestro's solution**: A deterministic **Generate → Validate → Fix** cycle:
1. **Generate**: Initial response following your requirements
2. **Validate**: Score each requirement (0.0 to 1.0)
3. **Fix**: Auto-refine outputs scoring < 1.0
4. **Repeat**: Until all requirements met or budget exhausted

## Key Concepts

- **Requirements**: Explicit constraints (format, content rules, business logic)
- **Budget Tiers**: Trade-off between cost/latency and reliability
  - `low`: Fast, fewer fix attempts
  - `medium`: Balanced
  - `high`: Maximum reliability, parallel processing
- **Requirements Report**: Detailed scores showing which constraints were met
- **Model Agnostic**: Works with any model you plug in

## When to Use Validated Output

### ✅ Use When
- Structured data extraction from unstructured text
- Strict format requirements (JSON schemas, specific layouts)
- Hallucination prevention is critical
- Compliance with explicit business rules
- API responses requiring exact specifications

### ❌ Skip When
- Creative/open-ended tasks
- Simple single-instruction prompts
- Flexibility > precision

## Demo: Travel Booking Data Extraction

### The Challenge
Extract structured booking info from conversational messages where:
- Information is incomplete (missing fields)
- Format is unstructured (natural language)
- Hallucination risk is high (model might "fill in" missing data)

**Critical constraint**: Never infer missing information. Use "NA" for unmentioned fields.

### Why MVO Matters Here
Standard LLMs will:
- Add years to partial dates despite instructions
- Guess at missing fields
- Ignore "use NA" requirements

Maestro's Validated Output:
- Enforces the "no hallucination" rule
- Validates format compliance
- Provides transparency via requirements report

### What You'll Build
A Python script that:
- Processes conversational booking messages
- Defines explicit extraction requirements
- Uses Maestro to extract data reliably
- Validates no unauthorized inferences
- Returns compliance scores

## Learning Objectives

By the end of this module:
1. Know when to use Validated Output vs standard LLM calls
2. Write clear, measurable requirements
3. Interpret requirements reports
4. Choose appropriate budget tiers
5. Implement production-grade extraction with hallucination prevention

---

**Next**: Hands-on coding with the AI21 Maestro Python SDK