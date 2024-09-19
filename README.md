# STOP
This is the repository for Sensitivity Testing on Offensive Progressions (STOP) {<-make hyperlink to arxiv when uploaded}, a dataset comprised of 450 offensive progressions designed to target evolving scenarios of bias and quanitfy the threshold of appropriateness. This work will be published in the 2024 Main Conference on Empirical Methods in Natural Language Processing.

Authors: Robert Morabito, Sangmitra Madhusudan, Tyler McDonald, Ali Emami

## Paper abstract
Mitigating explicit and implicit biases in Large Language Models (LLMs) has become a critical focus in the field of natural language processing. However, many current methodologies evaluate scenarios in isolation, without considering the broader context or the spectrum of potential biases within each situation. To address this, we introduce the Sensitivity Testing on Offensive Progressions (STOP) dataset, which includes 450 offensive progressions containing 2,700 unique sentences of varying severity that progressively escalate from less to more explicitly offensive. Covering a broad spectrum of 9 demographics and 46 sub-demographics, STOP ensures inclusivity and comprehensive coverage. We evaluate several leading closed- and open-source models, including GPT-4, Mixtral, and Llama 3. Our findings reveal that even the best-performing models detect bias inconsistently, with success rates ranging from 19.3\% to 69.8\%. We also demonstrate how aligning models with human judgments on STOP can improve model answer rates on sensitive tasks such as BBQ, StereoSet, and CrowS-Pairs by up to 191\%, while maintaining or even improving performance. STOP presents a novel framework for assessing the complex nature of biases in LLMs, which will enable more effective bias mitigation strategies and facilitates the creation of fairer language models.

## The datatset
Each offensive progression in STOP contains:
- `"prompts"`: a set of sentences that progress in exhibited bias.
- `"cfprompt"`: a counter-factual sentence that attempts to justify the biased content of the scenario.
- `"severity"`: the severity level of the progression.
- "`demographic`": the target demographic of the progression.
- "`sub_demographic"`: the target sub-demographic from the demographic.

## The file structure
- The file `STOP-full.json` contains all 450 offensive progressions for easy and robust assessment across demographics and severity levels.
- The file`STOP-full-labelled.json` also contains the entire dataset but with the evaluated model scores appended. 
- The folder `STOP-demographic` contains 9 subsets separated by **demographics**.
- The folder `STOP-severity` contains 3 subsets separated by **severity levels**.

## Reference
Please use the following bibtex citation if you use STOP in your work, thank you!
{add the arxiv reference, update once the acl anthology upload happens}
