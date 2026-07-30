# 3–5 Day Project-Based Roadmap: HTML + Django Templates
**Beginner → Job-Ready (Server-Side Rendering Focus)**

**Total Duration:** 3–5 days (intensive, 8–12 focused hours/day)  
**Core Philosophy:** Every concept is learned only by shipping real, deployable projects. You do not advance until the current phase is built, deployed (when appropriate), documented, tested, explained in your own words, and rebuilt from memory.

---

## Phase 1 – HTML Foundations & Semantic Structure
**Day 1 (8–10 hours)**

### Phase Overview
- **Goal:** Write clean, semantic, accessible HTML.
- **Estimated study time:** 8–10 hours
- **Prerequisites:** None
- **Expected outcome:** You can build a multi-page static website with perfect semantic structure and basic accessibility.

### Concepts
- HTML Document Structure (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`)
- Semantic Elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`, `<aside>`)
- Text, Lists, Links, Images + accessibility basics

### Practice
- Convert messy `<div>` soup into semantic HTML
- Build a personal “About Me” page
- Fix missing `alt` attributes and broken paths

### Python Mini Project
HTML Structure Validator & Pretty-Printer using BeautifulSoup

### Architecture Decision
No backend required (pure static HTML).

### Web + Mobile
- Static multi-page site
- React version (same semantic structure)
- React Native version (simple content mirror)

### Offline Support
Yes – Service Worker / Cache API (or just static files)

### Deployment
GitHub Pages, Netlify, or Cloudflare Pages

### Milestone Challenge
Build a complete Conference Landing Page with perfect semantics → Deploy → Rebuild from memory the next morning.

---

## Phase 2 – Forms, Tables, Media & Accessibility
**Day 2 (8–10 hours)**

### Phase Overview
- **Goal:** Master forms, media and accessibility (WCAG 2.1 AA).
- **Expected outcome:** You can build complex accessible forms.

### Concepts
- Forms & Form Controls + proper labels
- Tables (only for tabular data)
- Media + ARIA when needed

### Practice
- Convert a bad form into an accessible one
- Build a multi-step registration form
- Keyboard-only and screen-reader testing

### Python Mini Project
Form Data Simulator using Faker

### Architecture Decision
Still no backend (static forms for now).

### Milestone Challenge
Build a full Event Registration multi-page flow that works without JavaScript → Deploy → Rebuild from memory.

---

## Phase 3 – Django Setup & First Templates
**Day 3 (9–11 hours)**

### Phase Overview
- **Goal:** Move from static HTML into a real Django project and render dynamic templates.
- **Expected outcome:** Working Django project that serves HTML via templates with context.

### Concepts
- Django project & app structure
- Django Template Language basics (`{{ }}`, `{% %}`, filters, inheritance)
- Context & Views

### Practice
- Create context dictionaries and render them
- Build a simple Blog Post List view + template
- Fix TemplateDoesNotExist and missing context errors

### Python Mini Project
Context Builder function

### Architecture Decision
Yes – Django backend required.  
Stay on classic server-rendered templates. Optionally add a thin DRF API for React / React Native later.

### Milestone Challenge
Build a complete Personal Portfolio site in Django using template inheritance + dynamic project list + contact form that saves to the database → Deploy → Rebuild from memory the next day.

---

## Phase 4 – Advanced Django Templates + Production Project
**Days 4–5 (16–20 hours)**

### Phase Overview
- **Goal:** Master advanced DTL and ship a production-ready multi-page Django application.
- **Expected outcome:** Job-ready ability to build and maintain complex server-rendered Django apps.

### Concepts
- Deep template inheritance & composition
- Custom template tags & filters
- Django forms in templates + CSRF
- Static files, media, and basic template performance

### Practice
- Write custom template filters
- Build paginated list + detail pages
- Fix CSRF and static file issues in production-like settings

### Python Mini Project
Reusable custom template tag library

### Architecture Decision
Full Django backend + optional DRF API for mobile / SPA.

### Final Project Options
Choose one coherent product:
- Blog (categories, tags, search, comments)
- Job Board
- Portfolio + Blog + Contact system

Must include:
- Solid `base.html` + child templates
- Authentication (login/logout/register)
- Forms (create/update)
- Pagination
- Messages framework

### Milestone Challenge (Final)
Ship the complete deployed application.  
Then delete the project folder and rebuild the core (models + main templates + authentication) from memory in under 4 hours.

---

## Final Checklists

### Portfolio Checklist
- [x] At least 3 public GitHub repositories
- [x] Every repo has a clear README + live demo
- [x] Screenshots / short demo
- [x] “Rebuilt from memory” note in the final project

### GitHub Project Checklist
- [x] Meaningful commit history
- [x] Proper `.gitignore`
- [x] `requirements.txt` (or equivalent)
- [x] Clear folder structure
- [x] LICENSE

### Interview Preparation
- Explain the full request → view → template → response cycle
- Write a custom template tag on a whiteboard
- Discuss Django templates vs React SPA trade-offs
- Debug `TemplateDoesNotExist` and CSRF errors
- Sketch a solid `base.html` inheritance structure

### Recommended Resources
- Official Django Templates documentation
- MDN Web Docs (HTML + Accessibility)
- Django Girls Tutorial
- Real Python – Django templates articles
- WebAIM accessibility resources

### Common Interview Questions
1. Difference between `{{ variable }}` and `{% tag %}`
2. How template inheritance works
3. When to write a custom template tag vs putting logic in the view
4. How Django protects against XSS in templates
5. Purpose of `{% csrf_token %}`
6. How to organize templates in a large multi-app project
7. Server-side rendering with Django templates vs a React SPA

---

**Final Rule**  
You do not move to any advanced topics until every phase has been completed, deployed, documented, tested, explained in your own words, and successfully rebuilt from memory.
