# This Repository is for a submission

Tasks:
- Knowledge Base Creation (With RESTful APIs). 
Link to APIs: 

- Agent Conversation Flow (Using RetellAI)
Agent Linked Phone Number: 

## BBQ Nation Chatbot API

An AI-powered chatbot for Barbeque Nation, delivering accurate, context-aware responses to customer queries within an 800-token limit.

The code for this is included in this repository.

### Core Features

- **Query Classification:** Categorizes queries (menu, offers, timing, location etc.) using keywords.
- **Information Retrieval:** Fetches structured data from CSV knowledge bases.
- **Token Management:** Ensures responses stay under 800 tokens.
- **Error Handling:** Handles invalid inputs and provides fallback responses.
- **Feedback Logging:** Records customer feedback for improvements.
- **APIs:** RESTful endpoints for classification, info retrieval, and feedback.

### Technical Highlights

- **Data Management:** Cleans and validates CSV data.
- **Hallucination Prevention:** Strict validation and clear "not found" messages.

### Workflow

1. Customer submits a query.
2. System classifies and fetches relevant data.
3. Response is trimmed (if needed) and returned.

### Future Enhancements

- GPT integration for complex queries.
- Advanced search/filtering.
- Admin dashboard for data and feedback management.

## Agent Conversation Flow 

An AI-powered agent built specifically for Barbeque Nation, a restaurant chain. The agent was created using RetellAI to interact with customers and help them in several ways on **voice call**:

- Answering Questions: It can respond to customer queries about the restaurant’s menu, special offers, opening hours, and locations.
- Performing Tasks: The agent can assist with actions like booking a table or collecting customer feedback.
- Availability: Customers can interact with the agent over the phone.