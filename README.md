# LLM Finetuning: Generate Amharic text based creatives /Ad contents/
***

### Project Overview

An startup in Africa focused on AI and Blockchain business solutions needs to adjust its
advertising strategy to better fit this ever-changing ecosystem - in our case Telegram
messaging app.
For this project, We have the intention to improve the effectiveness of promotional efforts by
integrating powerful AI capabilities for Amharic text manipulation, in particular creating an
Amharic RAG pipeline that will help generate Amharic based creative text Ad contents given
campaign information such as brief (brand and product information) and the content history of
a telegram channel. This project makes sure that their advertisements are both catchy and
relevant to the Telegram community. To achieve this, it is required to have quality
**amharic text embedding** and **text generation**.

### Project Guide

After choosing a suitable open source LLM model with appropriate training and one that
should already have a capability to embed amharic texts, a dataset will be utilized to finetune it
further to deliver the business needs. That is made possible by using an efficient RAG system
to help generate ideal Ad contents in Amharic. The data contains exported Telegram messages
in JSON format representing 25 telegram public channels. The structure of the JSON object
provides information about the sender, timestamps, message types, and any associated
multimedia content.
In the end, A RAG pipeline will be set for the final Ad generation which will be hosted on
React.

### Approaches and Techniques
The data seems to be a dump and needs to be cleaned and preprocessed so as to get the
desired and ideal dataset to finetune the open source model. THe finetuning will take place in
two steps. It will be used to train the base model so it is possible to enable it to know more
Amharic Context, and then we will have a filtered and labeled dataset (filtered with Ad context
only) to help it understand Ads better and summarize it for us(It will generate a simple Ad).
Finally, we will have a RAG system with current campaigns and Brand or Product information
so it will generate a more likable, tailored and successful Ad.

### Usage
Clone the repo: git clone https://github.com/abrishdew/LLM-Finetuning_Generate-Amharic-based-creative-text-Ad-contents

Install dependencies: pip install -r requirements.txt

*CREATE YOUR ADS NOW!*

## License 



