# 🛑 STOP
This is the repository for "STOP! Benchmarking Large Language Models with Sensitivity Testing on Offensive Progressions" **{<-make hyperlink to arxiv when uploaded}**, a dataset comprised of 450 offensive progressions designed to target evolving scenarios of bias and quanitfy the threshold of appropriateness. This work will be published in the 2024 Main Conference on Empirical Methods in Natural Language Processing.

Authors: Robert Morabito, Sangmitra Madhusudan, Tyler McDonald, Ali Emami

## 📝 Paper abstract
Mitigating explicit and implicit biases in Large Language Models (LLMs) has become a critical focus in the field of natural language processing. However, many current methodologies evaluate scenarios in isolation, without considering the broader context or the spectrum of potential biases within each situation. To address this, we introduce the Sensitivity Testing on Offensive Progressions (STOP) dataset, which includes 450 offensive progressions containing 2,700 unique sentences of varying severity that progressively escalate from less to more explicitly offensive. Covering a broad spectrum of 9 demographics and 46 sub-demographics, STOP ensures inclusivity and comprehensive coverage. We evaluate several leading closed- and open-source models, including GPT-4, Mixtral, and Llama 3. Our findings reveal that even the best-performing models detect bias inconsistently, with success rates ranging from 19.3% to 69.8%. We also demonstrate how aligning models with human judgments on STOP can improve model answer rates on sensitive tasks such as BBQ, StereoSet, and CrowS-Pairs by up to 191%, while maintaining or even improving performance. STOP presents a novel framework for assessing the complex nature of biases in LLMs, which will enable more effective bias mitigation strategies and facilitates the creation of fairer language models.

## 📁 File structure
- The file `STOP-full.json` contains all 450 offensive progressions for easy and robust assessment across demographics and severity levels.
- The file`STOP-full-labelled.json` also contains the entire dataset but with the evaluated model scores appended. 
- The folders `STOP-demographic` contains 9 subsets separated by **demographics**.
  - The folder `STOP-demographic-labelled` is the same, but contains the evaluated model responses.
- The folder `STOP-severity` contains 3 subsets separated by **severity levels**.
  - The folder `STOP-severity-labelled` is the same, but contains the evaluated model responses.
- The `code` folder contains the code necessary for evaluating models on STOP.
  - `llmEvaluation.py` is the main program to run
  - `openaiHandler.py` and `anyscaleHandler.py` are helper classes for querying models via API calls
  - `ioFunction.py` is a helper function for loading and saving json files
  - `humanEvaluation.py` is the [tkinter](https://docs.python.org/3/library/tkinter.html) interface used for human testing

## 💾 Code and running instructions
The required packages for utilizing this code to evaluate models on STOP can be found in the `requirements.txt`. To install these packages simply use the command ``pip install -r requirements.txt``.
To reproduce the results of this paper, run the following command:
  ``python llmEvaluation.py --input_path <INPUT_PATH> --output_path <OUTPUT_PATH> --model <MODEL_NAME> --openai_key <OPENAI_API_KEY> --anyscale_key <ANYSCALE_API_KEY>
Where
- <INPUT_PATH>: The file path to the STOP dataset entries being used. This should be one of the provided JSON files from the dataset.
- <OUTPUT_PATH>: The file path to save the model responses to. This will save the the models sensitivity score and counter-factual responses, appended to each entry, as a JSON file.
- <MODEL_NAME>: The name of the model you wish to evaluate. The supported models and their names can be found using the help command below.
- <OPENAI_API_KEY>: Your personal OpenAI API key
- <ANYSCALE_API_KEY>: Your personal Anyscale API key

To get help with these, use the command ``python llmEvaluation.py -h`` for an explanation of each parameter.
All code and supported models were current as of March 2024.

## 📊 Dataset entries
Each offensive progression in STOP contains:
- `"prompts"`: a set of sentences that progress in exhibited bias.
- `"cfprompt"`: a counter-factual sentence that attempts to justify the biased content of the scenario.
- `"severity"`: the severity level of the progression.
- `"demographic"`: the target demographic of the progression.
- `"sub_demographic"`: the target sub-demographic from the demographic.

## 📖 Reference
Please use the following bibtex citation if STOP was apart of your work, thank you!
**{add the arxiv reference, update once the acl anthology upload happens}**
