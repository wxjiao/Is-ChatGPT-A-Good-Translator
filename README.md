# Is ChatGPT A Good Translator? A Preliminary Study [Updated for GPT-4!!!]

We conduct a preliminary evaluation of ChatGPT for machine translation. [[V1]](https://wxjiao.github.io/downloads/tech_chatgpt_arxiv.pdf) [[V2-ArXiv]](https://arxiv.org/abs/2301.08745v2)

This repository shows the main findings and releases the evaluated test sets as well as the translation outputs, for the replication of the study.


## Test Data
Please kindly cite the papers of the data sources if you use any of them.
- **Flores**: The FLORES-101  Evaluation Benchmark for Low-Resource and Multilingual Machine Translation
- **WMT19 Biomedical**: Findings of the WMT 2019 Biomedical Translation Shared Task: Evaluation for Medline Abstracts and Biomedical Terminologies
- **WMT20 Robustness**: Findings of the WMT 2020 Shared Task on Machine Translation Robustness


## Main Findings

### Translation Prompt

We ask ChatGPT for advice to trigger the translation ability:
<div align="center">
    <img width="70%" alt="Templates-by-ChatGPT" src="https://user-images.githubusercontent.com/31032829/213847658-fc977b1f-2ebd-4f2e-91b0-8df337d0a27e.png">
    <p class="image-caption">Figure 1: Prompts advised by ChatGPT for machine translation (Date: 2022.12.16).</p>
</div>

Summarized prompts:
- Tp1: `Translate these sentences from [SRC] to [TGT]:`
- Tp2: `Answer with no quotes. What do these sentences mean in [TGT]?`
- Tp3: `Please provide the [TGT] translation for these sentences:`

<div align="center">
    <img width="42%" alt="image" src="https://user-images.githubusercontent.com/31032829/213848303-4aa969c5-61d7-4dc8-b675-5a539657db67.png">
    <p class="image-caption">Table 1: Comparison of different prompts for ChatGPT to perform Chinese-to-English (Zh⇒En) translation.</p>
</div>


### Multilingual Translation

We evaluate the translations between four languages, namely, German, English, Romanian and Chinese, considering both the resource and language family effects:
<div align="center">
    <img width="70%" alt="image" src="https://user-images.githubusercontent.com/31032829/213848377-8c4d40d4-04de-4735-87fe-d22fd3f70dd9.png">
    <p class="image-caption">Table 2: Performance of ChatGPT for multilingual translation.</p>
</div>



### Pivot Prompting (Updates)

For distant languages, we explore an interesting strategy named **Pivot Prompting** that asks ChatGPT to translate the source sentence into a high-resource pivot language before into the target language. Thus, we adjust the Tp3 prompt as below:
- Tp3-pivot: `Please provide the [PIV] translation first and then the [TGT] translation for these sentences one by one:`

<div align="center">
    <img width="70%" alt="Pivot-Prompt" src="https://user-images.githubusercontent.com/31032829/215824464-cd16962e-1257-446f-a9ef-5909484fb4bc.png">
    <p class="image-caption">Figure 2: Translation results by ChatGPT with pivot prompting (Date: 2023.01.31).</p>
</div>

<div align="center">
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/31032829/215826297-2ae65654-d910-4fac-996b-834e6e6c7539.png">
    <p class="image-caption">Table 3: Performance of ChatGPT with pivot prompting. New results are obtained from the updated ChatGPT version on 2023.01.31. LR: length ratio.</p>
</div>


### Translation Robustness

We evaluate the translation robustness of ChatGPT on biomedical abstracts, reddit comments, and crowdsourced speeches:

<div align="center">
    <img width="52%" alt="image" src="https://user-images.githubusercontent.com/31032829/213848428-069891f5-4de0-4922-83f8-2f0c1b163d26.png">
    <p class="image-caption">Table 4: Performance of ChatGPT for translation robustness.</p>
</div>


## Limitations


We should admit that the report is far from complete with various aspects to make it more reliable in the future:
- **Coverage of Test Data**: Currently, we randomly select 50 samples from each test set for evaluation due to the response delay of ChatGPT. While there are some projects in GitHub trying to automate the access process, they are vulnerable to browser refreshes or network issues. The official API by OpenAI in the future may be a better choice. Let’s just wait for a moment.
- **Reproducibility Issue**: By querying ChatGPT multiple times, we find that the results of the same query may vary across multiple trials, which brings randomness to the evaluation results. For more reliable results, it is best to repeat the translation multiple times for each test set and report the average result.
- **Evaluation Metric**: The results here are calculated by automatic metrics with single references, which may not reflect some characteristics of translation properly, e.g., nativeness. Human evaluation can provide more insights for comparing ChatGPT with commercial translators.
- **Translation Abilities**: We only focus on multilingual translation and translation robustness in this report. However, there are some other translation abilities that can be further evaluated, e.g., constrained machine translation and document-level machine translation.



## Public Impact
### Community
- Slator: [Tencent Pits ChatGPT Translation Quality Against DeepL and Google Translate](https://slator.com/tencent-pits-chatgpt-translation-quality-against-deepl-google-translate/)

### Citation
Please kindly cite our report if you find it helpful:

```ruby
@inproceedings{jiao2023ischatgpt,
  title={Is ChatGPT A Good Translator? A Preliminary Study},
  author={Wenxiang Jiao and Wenxuan Wang and Jen-tse Huang and Xing Wang and Zhaopeng Tu},
  booktitle = {ArXiv},
  year      = {2023}
}
```
