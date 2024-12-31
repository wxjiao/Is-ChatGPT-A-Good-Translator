
<div align="center">
    <img width="25%" alt="ParroT" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/9ff13ff1-8e25-40bc-962e-80015cd82440">
    <h2>
    Is ChatGPT A Good Translator?
    </h2>
</div>

<!---
# Is ChatGPT A Good Translator? A Preliminary Study
--->

We conduct a preliminary evaluation of ChatGPT/GPT-4 for machine translation. [[V1]](https://wxjiao.github.io/downloads/tech_chatgpt_arxiv.pdf) [[arXiv]](https://arxiv.org/abs/2301.08745) 

This repository shows the main findings and releases the evaluated test sets as well as the translation outputs, for the replication of the study.



## ChatGPT for Machine Translation

### Test Data
Please kindly cite the papers of the data sources if you use any of them.
- [**Flores**](https://github.com/facebookresearch/flores): The FLORES-101  Evaluation Benchmark for Low-Resource and Multilingual Machine Translation
- [**WMT19 Biomedical**](https://github.com/hsing-wang/WMT2020_BioMedical/tree/master/Bio-18-19-testset): Findings of the WMT 2019 Biomedical Translation Shared Task: Evaluation for Medline Abstracts and Biomedical Terminologies
- [**WMT20 Robustness**](https://aclanthology.org/2020.wmt-1.4/): Findings of the WMT 2020 Shared Task on Machine Translation Robustness


### Translation Prompts

We ask ChatGPT for advice to trigger the translation ability:
<div align="center">
    <img width="70%" alt="Templates-by-ChatGPT" src="https://user-images.githubusercontent.com/31032829/213847658-fc977b1f-2ebd-4f2e-91b0-8df337d0a27e.png">
    <p class="image-caption">Figure 1: Prompts advised by ChatGPT for machine translation (Date: 2022.12.16).</p>
</div>

Summarized prompts:
- Tp1: `Translate these sentences from [SRC] to [TGT]:`
- Tp2: `Answer with no quotes. What do these sentences mean in [TGT]?`
- Tp3: `Please provide the [TGT] translation for these sentences:`  :white_check_mark:

<div align="center">
    <img width="42%" alt="image" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/d696165d-7ca7-4e6c-91a5-822f12e58f8f">
    <p class="image-caption">Table 1: Comparison of different prompts for ChatGPT to perform Chinese-to-English (Zh⇒En) translation.</p>
</div>


### Multilingual Translation

We evaluate the translations between four languages, namely, German, English, Romanian and Chinese, considering both the resource and language family effects.
- [x] ChatGPT performs competitively with commercial translation products (e.g., Google Translate) on high-resource European languages but lags behind significantly on low-resource.
- [x] The gap between ChatGPT and the commercial systems becomes larger on distant languages than close languages. 

<div align="center">
    <img width="70%" alt="image" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/bff8f331-76d8-4d97-a3f7-0c7cd536d62f">
    <p class="image-caption">Table 2: Performance of ChatGPT for multilingual translation.</p>
</div>


### Translation Robustness

We evaluate the translation robustness of ChatGPT on biomedical abstracts, reddit comments, and crowdsourced speeches.
- [x] ChatGPT does not perform as well as the commercial systems on biomedical abstracts or Reddit comments but exhibits good results on spoken language.

<div align="center">
    <img width="42%" alt="image" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/9eec7ce9-16f5-4d3e-80ce-cae67bc647e1">
    <p class="image-caption">Table 3: Performance of ChatGPT for translation robustness.</p>
</div>



## Improving ChatGPT for MT

### Pivot Prompting

For distant languages, we explore an interesting strategy named **Pivot Prompting** that asks ChatGPT to translate the source sentence into a high-resource pivot language before into the target language. Thus, we adjust the Tp3 prompt as below:
- Tp3-pivot: `Please provide the [PIV] translation first and then the [TGT] translation for these sentences one by one:`

<div align="center">
    <img width="70%" alt="Pivot-Prompt" src="https://user-images.githubusercontent.com/31032829/215824464-cd16962e-1257-446f-a9ef-5909484fb4bc.png">
    <p class="image-caption">Figure 2: Translation results by ChatGPT with pivot prompting (Date: 2023.01.31).</p>
</div>

<div align="center">
    <img width="40%" alt="image" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/6e92f8a4-44e9-4ce3-b295-78249cc032c5">
    <p class="image-caption">Table 4: Performance of ChatGPT with pivot prompting. New results are obtained from the updated ChatGPT version on 2023.01.31. LR: length ratio.</p>
</div>


### GPT-4 as the Engine

We update the translation performance of GPT-4, which exhibits huge improvements over ChatGPT. Refer to [[ParroT]](https://github.com/wxjiao/ParroT) for the COMET metric results.

<div align="center">
    <img width="70%" alt="Templates-by-ChatGPT" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/1297c121-33d8-4b5f-9cad-7eb09b75f97f">
    <p class="image-caption">Table 5: Translation performance of GPT-4 (Date: 2023.03.15). </p>
</div>


## Extensive Analysis

### Automatic Analysis
We analyze the translation outputs with [`compare-mt`](https://github.com/neulab/compare-mt) at both word level and sentence level.
- [x] ChatGPT performs the worst on low-frequency words, which is then fixed by GPT-4.
- [x] ChatGPT performs the worst on short sentences, which we attribute to the observations that ChatGPT translates famous terminologies into full names rather than abbreviations in references.  

<div align="center">
    <img width="35%" alt="auto" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/6fcb3a76-827a-4335-9e8d-b7dd73aca8c5">
    <img width="35%" alt="auto" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/3ea1a67b-bb34-4098-bd5f-52736f11f0e4">
    <p class="image-caption">Table 6-7: Automatic analysis: (a) F-measure of target word prediction w.r.t. frequency. (b) BLEU score w.r.t. length bucket of target sentences. </p>
</div>


### Human Analysis
We ask three annotators to identify the errors in the translation outputs, including under-translation, over-translation, and mis-translation. Based on the translation errors, the annotators rank the translation outputs of Google, ChatGPT and GPT-4 accordingly, with 1 as the best system and 3 as the worst. 
- [x] ChatGPT makes more over-translation errors and mis-translation errors than Google Translate, tending to generate hallucinations.
- [x] GPT-4 makes the least errors and is ranked 1st though its BLEU score is lower than that of Google Translate.

<div align="center">
    <img width="35%" alt="auto" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/197d3268-ca84-476e-bb37-b31ecf6e5206">
    <img width="35%" alt="auto" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/55f05725-3bd8-4d2e-9025-4684f58739b8">
    <p class="image-caption">Table 8-9: Human analysis: (a) Number of translation errors annotated by human. (b) Human rankings of the translation outputs. </p>
</div>


### Case Study

A few translation outputs:
1. ChatGPT hallucinates at the first few tokens and also mis-translates "过量降水".
2. Both ChatGPT and GPT-4 translate "广泛耐药结核病" into the full name while the reference and Google Translate do not.
3. GPT-4 can translate the terminology "美国公共广播公司" into the abbreviation as the reference.
4. GPT-4 translates the terminology "狼孩" more properly based on the context while Google Translate and ChatGPT cannot.

<div align="center">
    <img width="90%" alt="Cases" src="https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator/assets/31032829/b6e9a278-0268-4df5-b2f4-30e8b382d476">
    <p class="image-caption">Table 10: Examples from Flores Zh⇒En test set. </p>
</div>


## Limitations

We should admit that the report is far from complete with various aspects to make it more reliable in the future:
- **Coverage of Test Data**: Currently, we randomly select 50 samples from each test set for evaluation due to the response delay of ChatGPT. While there are some projects in GitHub trying to automate the access process, they are vulnerable to browser refreshes or network issues. The official API by OpenAI in the future may be a better choice. Let’s just wait for a moment.
- **Reproducibility Issue**: By querying ChatGPT multiple times, we find that the results of the same query may vary across multiple trials, which brings randomness to the evaluation results. For more reliable results, it is best to repeat the translation multiple times for each test set and report the average result.
- **Translation Abilities**: We only focus on multilingual translation and translation robustness in this report. However, there are some other translation abilities that can be further evaluated, e.g., constrained machine translation and document-level machine translation.



## Public Impact

[![Star History Chart](https://api.star-history.com/svg?repos=wxjiao/Is-ChatGPT-A-Good-Translator&type=Date)](https://star-history.com/#wxjiao/Is-ChatGPT-A-Good-Translator&Date)


### Community
- Slator report: [Tencent Pits ChatGPT Translation Quality Against DeepL and Google Translate](https://slator.com/tencent-pits-chatgpt-translation-quality-against-deepl-google-translate/)
- Twitter discussions: [AK](https://twitter.com/_akhaliq/status/1617710116827963392), [Aran Komatsuzaki
](https://twitter.com/arankomatsuzaki/status/1617708239906549761), [Haruhiko Okumura
](https://twitter.com/h_okumura/status/1638079006351437824), [Daun](https://twitter.com/daun_ai/status/1648083948562690050)

### Citation
Please kindly cite our report if you find it helpful:

```ruby
@inproceedings{jiao2023ischatgpt,
  title={Is ChatGPT A Good Translator? A Preliminary Study},
  author={Wenxiang Jiao and Wenxuan Wang and Jen-tse Huang and Xing Wang and Shuming Shi and Zhaopeng Tu},
  booktitle = {ArXiv},
  year      = {2023}
}
```
