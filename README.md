# LLM Finetuning: Generate Amharic-based Creative Text Ad Contents

<img src="https://camo.githubusercontent.com/3cefee189432defff4cb59838ead898a2bd661cd4b475e25391c87edd2241782/68747470733a2f2f7374617469632e7769787374617469632e636f6d2f6d656469612f3038316535625f35353533383033666465656334636262383137656434653835653138393962327e6d76322e706e672f76312f66696c6c2f775f3234362c685f3130362c616c5f632c715f38352c75736d5f302e36365f312e30305f302e30312c656e635f6175746f2f313025323041636164656d7925323046412d30322532302d2532307472616e73706172656e742532306261636b67726f756e642532302d25323063726f707065642e706e67">

***

## Project Overview

Given Telegram's growing prominence as a messaging platform, AiQEM (an African startup focused on AI and Blockchain business solutions) needs to adjust its advertising strategy to better fit this ever-changing ecosystem. This project intends to improve the effectiveness of their promotional efforts by integrating powerful AI capabilities for Amharic text manipulation, particularly creating an Amharic RAG pipeline that will help generate Amharic-based creative text Ad contents given campaign information such as brief (brand and product information) and the content history of a Telegram channel.

This project ensures that their advertisements are both catchy and relevant to the Telegram community. To achieve this, the technology is required to have quality **Amharic text embedding** and **text generation** capability.

## Project Guide

In order to generate content which is both targeted and sensible Ads, the model needs to be trained on a large Amharic language corpus. To guide the model in that direction, the steps are classified into two:

### 1. Supervised Training

The project follows two steps. The first step is to classify the dataset between Ad and Non-Ad based on the score. The supervised training will further be continued to train based on each tag/label to classify them correctly.

#### Outcomes

The outcomes of the supervised training, including any relevant screenshots, are located inside the ["semi-supervised_training(Mistral 7B)/screenshots"](semi-supervised_training(Mistral%207B)/screenshots) folder.


### 2. RAG (Retriever, Generator, and Query)

The RAG part has components of retriever, craft the prompt, and finally query.

- **Retriever:** The context is going to be extracted from public channel conversational history and used as context to make it a highly personalized promotional text that resonates with the channel, drawing insights from their contextual data. Leverage historical interactions, discussions, or online activities to tailor the ad closely to context unique preferences and interests.

- **Craft the Prompt:** Will guide the model to generate Amharic Ads based on queries which include brand description, services, and products.
- **Query:** The query will take an input query which is brand product and services to be advertised 

