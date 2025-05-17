# This Repository is for a submission

Tasks:
### Knowledge Base Creation (With RESTful APIs).

**Link to APIs:**

The following APIs are available for the BBQ Nation Chatbot:

- [Classify Query](http://127.0.0.1:8000/classify) - Classifies customer queries into categories like menu, address, facilities, etc.
- [Retrieve Information](http://127.0.0.1:8000/info) - Fetches specific information based on customer queries.
- [Raw Data Retrieval](http://127.0.0.1:8000/raw) - Retrieves raw information from the knowledge base.
- [Nearest Outlets](http://127.0.0.1:8000/raw/nearest) - Finds the nearest outlets for a given city.
- [Feedback Submission](http://127.0.0.1:8000/feedback) - Logs customer feedback for analysis.

You can explore and test the APIs using the Swagger UI:

- [Swagger UI](http://127.0.0.1:8000/docs) - Interactive API documentation.
- [ReDoc](http://127.0.0.1:8000/redoc) - Alternative API documentation.

Note: The above links are for local testing.

### Agent Conversation Flow (Using RetellAI).

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

### How it was done
- Converted all knowledge base pdfs to raw text using python script.
- Converted this text dump to csv and json form using Perplexity.
- Wrote the code for the app (using above csv files as data) and used test_api.py to test the endpoints.

## Agent Conversation Flow 

An AI-powered agent built specifically for Barbeque Nation, a restaurant chain. The agent was created using RetellAI to interact with customers and help them in several ways on **voice call**:

- Answering Questions: It can respond to customer queries about the restaurant’s menu, special offers, opening hours, and locations.
- Performing Tasks: The agent can assist with actions like booking a table or collecting customer feedback.
- Availability: Customers can interact with the agent over the phone.

### How it was done:

- Used the above data and converted to formatted and proper text using perplexity.
