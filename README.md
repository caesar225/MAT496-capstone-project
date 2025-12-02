# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

## Title: News Article Bias Checker Using LangGraph

A LangGraph-powered system for detecting media bias, comparing coverage, and analyzing narratives in news articles.

## Overview

This project implements a News Article Bias Checker.
The system ingests multiple news articles on the same topic, uses semantic search, RAG, and LLM-based structured analysis to detect:

Political leaning / stance

Sentiment toward subjects

Framing differences

Missing context

Comparison across sources

Potential ideological bias

Built using LangGraph, the pipeline consists of nodes that ingest articles, embed them, retrieve related content, and produce a structured bias report.
This project demonstrates how LLMs can analyze large amounts of text and extract meaningful insights that would be difficult to detect manually.

## Reason for picking up this project

This project is directly aligned with the major concepts covered in the course:

Prompting: Bias analysis, classification, comparison prompts

Structured Output: JSON reports summarizing bias, sentiment, and framing

Semantic Search: Grouping articles discussing the same event

Retrieval-Augmented Generation (RAG): Ensuring the model cites from the articles

Tool Calling & MCP: Optional integration for fetching live news

LangGraph Concepts:

State management

Multi-node workflows

Conditional branches (e.g., missing context detection)

This project also reflects how LLMs can automate tasks that require extensive reading and comparison, demonstrating a real-world application of the course concepts.


## Plan

I plan to execute these steps to complete my project.

- [DONE] Step 1- Initialize LangGraph Project

Create project structure

Define the global graph state (articles, embeddings, clusters, analysis results)

- [DONE] Step 2- Article Ingestion Node

Accept text files, URLs, or raw text

Clean and normalize article content

Store metadata (source, date, author if available)

- [DONE] Step 3- Embeddings + Vector Store Setup

Convert articles into embeddings

Store them in FAISS or Chroma

Prepare semantic grouping logic
- [DONE] Step 4- Semantic Grouping Node

Identify which articles discuss the same event

Cluster articles using vector similarity

This enables cross-source comparison

- [DONE] Step 5- Retrieval Node (RAG)

For each cluster, retrieve relevant snippets

Ground the LLM’s reasoning in actual article text

- [DONE] Step 6- Bias Analysis Node

Using structured prompts, extract:

Source political leaning (if known)

Sentiment toward key subjects

Framing type (positive, negative, neutral)

Mentions of loaded language or emotional framing

Coverage imbalance (what some sources include/exclude)

- [DONE] Step 7- Cross-Source Comparison Node

Compare coverage between left, center, and right-leaning outlets

Identify missing context bias

Highlight narrative differences

- [DONE] Step 8- Report Generation Node

Output in Markdown or JSON:

Summary of the event

Bias score per article

Coverage comparison table

Key excerpts supporting each bias detection

Visual indicators (optional)

- [TODO] Step 9- UI or CLI

Build a simple user interface to upload articles and view the bias report dynamically

# How to run the Project: 

1) Install dependencies: pip install -r requirements.txt
2) Run the program: python main.py

# How to provide input:

The News Bias Checker supports interactive input from the command line.
When you run the program, you can choose between:

Option 1 — Paste Article Text Manually

You will be prompted to paste any number of articles directly into the terminal.

Option 2 — Provide File Paths

You can supply .txt files that contain the articles.

Example files may look like:
data/article1.txt
data/article2.txt

Once processing is done, you’ll see a final report.

# How the Agent works:

When the user provides articles, the system runs them through a LangGraph pipeline of nodes. Each node performs one specific task, and all results are stored in a shared global state.

1) Ingestion- The agent reads the article text (pasted or from files), cleans it, and stores metadata like source name.
2) Embeddings- Each article is converted into a semantic embedding vector using sentence-transformers.
3) Semantic Grouping- Using vector similarity, the agent clusters articles that discuss the same event.
4) Retrieval(RAG)- For each group, the agent retrieves the most relevant sentences and excerpts to ground the LLM’s reasoning.
5) Bias Analysis- Groq’s Llama-3.3-70B analyzes each article using structured prompts, extracting: Sentiment, Framing, Loaded language, missing context and overall bias score.
6) Cross Source Comparison- Articles within each cluster are compared by narrative style and political leaning.
7) Report Generation- Final bias report shown to the user. Ex-

   <img width="1903" height="772" alt="image" src="https://github.com/user-attachments/assets/27d4ffbf-ad86-4802-b67e-bbdf095c0630" />


## Conclusion:

The goal of this project was to build a complete Bias Checker System using concepts from the course: prompting, structured output, semantic search, RAG, tool calling, and LangGraph workflows.
I believe I successfully achieved the objectives. The system is able to:

Ingest multiple news articles

Group them by topic using semantic similarity

Analyze bias and sentiment

Compare framing across different news sources

Produce a structured, interpretable report

This project demonstrates how LLMs can handle complex analytical tasks such as media bias detection, which traditionally requires extensive human reading and interpretation. Overall, the system is functional, extensible, and a strong demonstration of concepts learned throughout the course. I would have liked to make the UI a lot better though.


