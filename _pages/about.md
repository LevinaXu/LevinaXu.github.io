---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  dl {
    margin-bottom: 60px; /* 调整这个值以获得合适的间距 */
    clear: both;
  }

  /* 全局文本颜色 */
  body {
    color: #333; /* 主要文本颜色 */
    background-image: url('../images/bg.jpg'); /* 背景图片 */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
  }

  /* 链接颜色 */
  a {
    color: #0066cc; /* 链接颜色 */
  }

  /* 作者名字颜色 */
  strong {
    color: #000; /* 作者名字颜色 */
  }

  /* 年份标题颜色 */
  .year-title {
    color: #666;
  }

  /* 会议标签样式 */
  .conference-label {
    position: absolute;
    top: 10px;
    left: -5px;
    background-color: #2c3e50;  /* 深蓝色背景 */
    color: white;  /* 白色文字 */
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.95em;
    font-weight: 600;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    z-index: 1;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-style: italic;  /* 添加斜体 */
  }

  /* 鼠标悬停效果 */
  .conference-label:hover {
    background-color: #34495e;  /* 悬停时稍微变亮 */
    transition: background-color 0.2s ease;
  }

  dl dt img {
    width: 100%; /* 在移动端默认占满宽度 */
    aspect-ratio: 2/1; /* 设置宽高比为2:1，即高度为宽度的一半 */
    object-fit: cover; /* 确保图片不会被裁剪 */
    display: block;
    margin: 10px 10px 10px 0px; /* 适当的间距 */
    
    /* 添加美化效果 */
    border-radius: 8px; /* 让图片有轻微的圆角 */
    border: 2px solid #ddd; /* 添加淡灰色的边框 */
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); /* 添加轻微阴影 */
    padding: 5px; /* 给图片一些内边距，让它不贴着边框 */
    background-color: #fff; /* 设置背景色，让图片更加干净 */
  }

  /* 在桌面端（宽度大于768px）时固定宽度 */
  @media screen and (min-width: 768px) {
    dl dt img {
      width: 350px;
    }
  }

  dl dt {
    position: relative;
  }

  hr {
    border: 1px solid #ebebeb; /* 调整分隔线的颜色和样式 */
    /* margin: 10px;  */
    clear: both; 
  }

  dl dd {
  margin-top: 5px; 
  margin-bottom: 5px;
}

  dl dd strong {
  font-weight: bold;
  color: black;
  }

  .co-first {
    color: red;
  }

  .down {
    transform: rotate(180deg);
  }

  /* 教育和工作经历卡片样式 */
  .experience-card, .education-card {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-bottom: 30px;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: 1px solid #e9ecef;
  }

  .experience-card:hover, .education-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border-color: #dee2e6;
  }

  .experience-info, .education-info {
    flex: 1;
  }

  .experience-logo, .education-logo {
    flex-shrink: 0;
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .experience-logo img, .education-logo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .experience-title, .education-title {
    font-size: 1.2em;
    margin-bottom: 8px;
    color: #2c3e50;
  }

  .experience-title a, .education-title a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .experience-title a:hover, .education-title a:hover {
    color: #3498db;
  }

  .experience-role, .education-role {
    color: #666;
    font-style: italic;
    margin-bottom: 5px;
  }

  .experience-topics, .education-topics {
    color: #666;
    font-style: italic;
  }

  .section-title {
    font-size: 1.8em;
    color: #2c3e50;
    margin: 40px 0 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #ecf0f1;
  }

  /* 奖学金和荣誉部分样式 */
  .honors-list {
    list-style: none;
    padding: 0;
  }

  .honors-list li {
    margin-bottom: 15px;
    padding: 15px 20px;
    background: #f8f9fa;
    border-radius: 8px;
    border-left: 4px solid #3498db;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .honors-list li:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .honors-list li strong {
    color: #2c3e50;
  }

  .honors-list li a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .honors-list li a:hover {
    color: #2980b9;
  }

  /* 服务部分样式 */
  .service-section {
    margin-bottom: 30px;
  }

  .service-section h3 {
    color: #2c3e50;
    font-size: 1.3em;
    margin: 25px 0 15px;
    padding-bottom: 8px;
    border-bottom: 2px solid #ecf0f1;
  }

  .service-list {
    list-style: none;
    padding: 0;
  }

  .service-list li {
    margin-bottom: 12px;
    padding: 12px 15px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
  }

  .service-list li:hover {
    transform: translateX(5px);
  }

  .service-list li a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .service-list li a:hover {
    color: #2980b9;
  }
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>


My name is Levina Mengting Li, a senior student at University of California, Los Angeles ([UCLA](https://www.ucla.edu/)), while I’m doing research supervised by [Kai-Wei Chang](https://scholar.google.com/citations?user=fqDBtzYAAAAJ&hl=zh-CN)  and [Ying Nian Wu](https://scholar.google.com/citations?user=7k_1QFIAAAAJ&hl=zh-CN&oi=ao), working closely with [Eric Hanchen Jiang](https://ericjiang18.github.io/).



<!-- 
<div style="text-align: left; margin: 20px 0;">
  <img src="../images/sign.png" alt="Signature" style="max-width: 150px; height: auto;">
</div> -->


<!-- 
<div style="background: linear-gradient(135deg, #f3f8ff, #e8f4fd); padding: 20px; border-radius: 10px; margin: 20px 0; border: 2px solid #1976d2; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); position: relative; overflow: hidden;">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.3)); pointer-events: none;"></div>
  <p style="margin: 0; position: relative; z-index: 1;"> <strong style="color: red">🌟 📢 Seeking for Remote Intern/Assistant (RA)</strong><br>
We are looking for motivated research interns to work together! Almost every intern who worked with me has published papers at top conferences such as ICML, NeurIPS, ICLR and CVPR. If you are interested, please don't hesitate to contact me via <a href="mailto:gcwan03@ucla.edu">Email</a> or <a 
href="https://guanchengwan.github.io/images/wechat.png">WeChat</a>.
  </p>
</div> -->


# 🔎 Research 
<!-- "All things are interconnected, this is the essence of nature."  -->

<!-- <dt style="text-align: center; margin: 0; padding: 0;">
  <img src="../images/research.png" style="display: block; max-width: 700px; width: 100%; height: auto; margin: 0 auto;">
</dt> -->

My current research interests focus on these key areas: 


a) Large Language Models (LLM), LLM Agent, LLM Agentic Systems,  Large Reasoning Models

b) AI for Science/Healthcare





<!-- 

# 🔥 News

<div style="max-height: 350px; overflow-y: auto; padding: 20px; background: #f8f9fa; border-left: 4px solid #2c3e50; margin: 0px 0;">
<style>
  /* 为 Webkit 浏览器（Chrome, Safari, Edge）设置滚动条样式 */
  div::-webkit-scrollbar {
    width: 8px;
  }

  div::-webkit-scrollbar-track {
    background: #e9ecef;
    border-radius: 4px;
  }

  div::-webkit-scrollbar-thumb {
    background: #2c3e50;
    border-radius: 4px;
  }

  div::-webkit-scrollbar-thumb:hover {
    background: #1a252f;
  }

  /* 为 Firefox 设置滚动条样式 */
  div {
    scrollbar-width: thin;
    scrollbar-color: #2c3e50 #e9ecef;
  }
</style>
<ul style="list-style-type: none; padding-left: 0; margin: 0;">
  <li><em>2025.09.20:</em> 🎉 Several papers were accepted by <strong>NeurIPS 2025</strong> with <strong class="co-first"> Two Spotlights (Top 3.1%)</strong>. See you in San Diego!</li>
  <li><em>2025.09:</em> 🎉 One paper was accepted by <strong>EMNLP 2025 Findings</strong>. Thanks to all collaborators!</li>
  <li><em>2025.05:</em> 🎉 Two papers were accepted by <strong>ACL 2025 Main</strong>. Thanks to all collaborators!</li>
  <li><em>2025.05:</em> 🎉 Some papers were accepted by <strong>ICML 2025</strong> with <strong class="co-first"> Two Spotlights (Top 2.6%)</strong>. See you in Vancouver!</li>
   <li><em>2024.11:</em> 🫡 Serve as Associate <strong>Program Chair</strong> for <a href="https://fedkdd.github.io/fedkdd2025/">FedKDD 2025@KDD</a> - Welcome to submit!</li>
  <li><em>2025.04:</em> 🎉 One co-first authored paper: LoRASculpt was selected as an <strong class="co-first">Oral Presentation (Top 3.3%)</strong> at <strong>CVPR 2025</strong>. Thanks to all collaborators!</li>
  <li><em>2025.03:</em> 🎉 One co-first authored paper: FedTGE was selected as an <strong class="co-first">Oral Presentation (Top 1.8%)</strong> at <strong>ICLR 2025</strong>. Thanks to all collaborators!</li>
  <li><em>2025.02:</em> 🎉 Three papers accepted by <strong>CVPR 2025</strong> on fine-tuning and applications of <strong>Multimodal Large Language Models (MLLM)</strong>. Thanks to all collaborators! See you in Nashville.</li>
  <li><em>2024.02:</em> I serve as a reviewer for <strong>NeurIPS 2025</strong>.</li>
  <li><em>2024.02:</em> 🎉 Honored to receive Graduate Research Fellowship from <strong>UCLA</strong> and <strong>UIUC</strong>.</li>
  <li><em>2025.01:</em> 🎉 Two papers were accepted by <strong>ICLR 2025</strong>. See you in Singapore.</li>
  <li><em>2024.12:</em> 🎉 One paper was accepted by <strong>AAAI 2025</strong>.</li>
  <li><em>2024.12:</em> I serve as a reviewer for <strong>ICML 2025</strong>.</li>
  <li><em>2024.11:</em> 🎈I was honored with <strong>Lei Jun Excellence Scholarship</strong> ~ <strong>100k</strong> (The <strong><u>Highest</u></strong> Scholarship at Wuhan University, <strong><u>Top-4</u></strong> among All Undergraduates, Award Rate ~ <strong>0.01%</strong>)</li>
  <li><em>2024.11:</em> I serve as a reviewer for <strong>CVPR 2025</strong>.</li>
  <li><em>2024.09:</em> 🎉 Two papers were accepted by <strong>NeurIPS 2024</strong>. See you in Vancouver.</li>
  <li><em>2024.08:</em> Organize a tutorial at <strong>KDD 2024</strong> in Barcelona on 25th, come if you are interested in epidemics + GNN!</li>
  <li><em>2024.08:</em> I serve as a reviewer for <strong>ICLR 2025</strong>.</li>
  <li><em>2024.06:</em> 🎉 One paper is accepted by <strong>TPAMI</strong>, congrats to all collaborators!</li>
  <li><em>2024.05:</em> I serve as a reviewer for <strong>NeurIPS 2024</strong>.</li>
  <li><em>2024.05:</em> 🎉 Our survey about GNNs in Epidemic Modeling is accepted by <strong>KDD 2024</strong>. See you in Barcelona!</li>
  <li><em>2024.05:</em> 🎉 One paper about self-supervised graph learning was accepted by <strong>ICML 2024</strong>. See you in Austria!</li>
  <li><em>2024.04:</em> 🚀 Explore our pre-print: a deep look at using Graph Neural Networks in Epidemic Modeling. Check our collected <a href="https://github.com/Emory-Melody/awesome-epidemic-modeling-papers">paper list</a>.</li>
  <li><em>2024.02:</em> I serve as a reviewer for <strong>ACM MM 2024</strong>.</li>
  <li><em>2024.02:</em> I serve as a reviewer for <strong>ECCV 2024</strong>.</li>
  <li><em>2023.12:</em> A paper was accepted to <strong>AAAI 2024</strong>. See you in Vancouver.</li>
  <li><em>2023.11:</em> I serve as a reviewer for <strong>CVPR 2024</strong>.</li>
  <li><em>2023.11:</em> 🚀 We thoroughly explore three core research areas in federated learning: generalization, robustness, and fairness. Don't hesitate to utilize our <a href="https://github.com/WenkeHuang/MarsFL">benchmarking codes</a> for your own research goal!</li>
  <li><em>2023.10:</em> I attended China National Computer Congress (CNCC) and was awarded the honor of CCF (China Computer Federation) Elite Collegiate Award (102 Students nation-wide).</li>
  <li><em>2023.10:</em> I won the National Scholarship for the second time (0.2% nation-wide), and was selected the Pacemaker to Merit Student (Award Rate: 60/59774=0.1%).</li>
  <li><em>2023.08:</em> we attended <em>the 32nd international joint conference on artificial intelligence (<strong>ijcai</strong>)</em> and presented our work in macao.</li>
</ul>
</div>

<br/>

 -->

<!-- 


# 📝 Manuscripts

<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/DLA.png">
<span class="conference-label">Arxiv</span>
</dt>
  <dd><a href="https://arxiv.org/pdf/2509.23188"><strong>Diagnose, Localize, Align: A Full-Stack Framework for Reliable LLM Multi-Agent Systems under Instruction Conflicts</strong></a></dd>
<dd>Arxiv: 2509.23188</dd>
</dl>

<hr>


<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/TARE.png">
<span class="conference-label">Arxiv</span>
</dt>
  <dd><a href="https://arxiv.org/pdf/2509.24130"><strong>Beyond Magic Words: Sharpness-Aware Prompt Evolving for Robust Large Language Models with TARE</strong></a></dd>
<dd>Arxiv: 2509.24130</dd>
</dl>

<hr> 





 -->


# 📃 Publications

**&dagger; Equal Contribution (Co-first listed in random order)**   

<div style="text-align: left; margin: 20px 0; font-size: 1.5em; color: #666;">
2025 
</div>

<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/GTD.png">
</dt>
  <dd><a href="https://arxiv.org/abs/2510.07799"><strong>	
GTD: Dynamic Generation of Multi LLM Agents Communication Topologies with Graph Diffusion Models
</strong></a></dd>
<dd><strong>Mengting Li&dagger;</strong>, Eric Hanchen Jiang&dagger;, Guancheng Wan&dagger;, Sophia Yin&dagger;,  Yuchen Wu, Xiao Liang, Xinfeng Li, Yizhou Sun, Wei Wang, Kai-Wei Chang, Ying Nian Wu</dd>
<dd> Submitted to ICLR, 2025</dd>
</dl>



<hr>



<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/LENS.png">

</dt>
  <dd><a href=""><strong> 
LENS: Learning Architecture Navigator for LLM Agentic Systems
</strong></a></dd>
<dd><strong>Mengting Li&dagger;</strong>, Guancheng Wan&dagger;, Jiayi Yang&dagger;, Eric Hanchen Jiang, Haixin Wang, Hui Yi Leong, Yizhou Sun, Wei Wang</dd>
<dd> Accepted to <strong>AAAI 2026</strong> @ Foundations of Agentic Systems Theory</dd>
<dd>Accepted to <strong>AAAI 2026</strong> @ Agentic AI Benchmarks and Applications for Enterprise Tasks</dd>
<dd>Submitted to ACL Rolling Review, 2025</dd>
</dl>


<hr>



<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/RAAS.png">

</dt>
  <dd><a href=""><strong> 
RAAS: LLM Agentic System Architecture Search with GRPO
</strong></a></dd>
<dd><strong>Mengting Li&dagger;</strong>, Jiayi Yang&dagger;, Guancheng Wan&dagger;, Wenke Huang, Jinhe Bi, Han Zhang, Eric Hanchen Jiang, Yizhou Sun, Wei Wang</dd>
<dd>Accepted to <strong>AAAI 2026</strong> @ Agentic AI Benchmarks and Applications for Enterprise Tasks</dd>
<dd>Submitted to ACL Rolling Review, 2025 </dd>
</dl>

<hr>



<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/DLA.png">

</dt>
  <dd><a href=""><strong> 
Diagnose, Localize, Align: A Full-Stack Framework for Reliable LLM Multi-Agent Systems under Instruction Conflicts
</strong></a></dd>
<dd><strong>Mengting Li&dagger;</strong>, Guancheng Wan&dagger;, Leixin Sun&dagger; </dd>
<dd>Accepted to <strong> 2025</strong> @ Socially Responsible and Trustworthy Foundation Models</dd>
<dd>Accepted to <strong>NeurIPS 2025</strong> @ LLM Persona Modeling</dd>
<dd>Submitted to ICLR, 2026 </dd>
</dl>

<hr>




<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/TARE.png">

</dt>
  <dd><a href=""><strong> 
Beyond Magic Words: Sharpness-Aware Prompt Evolving for Robust Large Language Models with TARE
</strong></a></dd>
<dd><strong>Mengting Li&dagger;</strong>, Guancheng Wan&dagger;, Lucheng Fu&dagger; </dd>
<dd>Accepted to <strong>NeurIPS 2025</strong> @ NORA: The First Workshop on Knowledge Graphs & Agentic Systems Interplay</dd>
<dd>Submitted to ICLR, 2026 </dd>
</dl>

<hr>


<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/DPOG.png">

</dt>
  <dd><a href=""><strong> 
Graph Representation Learning as Policy Optimization from Implicit Preferences
</strong></a></dd>
<dd>Chunhe Wang, Eric Hanchen Jiang, Guancheng Wan, Jingbang Chen, Zitong Shi, Andrew Lizarraga, <strong>Mengting Li</strong>, Wenxiao Zhao, Maggie Cheng, Ying Nian Wu</dd>
<dd> Submitted to AAAI, 2026</dd>
</dl>


<hr>




<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/Latent.png">
</dt>
  <dd><a href=""><strong> 
Optimizing Strategy, Not Scripts: Latent Plan Control for LLM Agents
</strong></a></dd>
<dd>Eric Hanchen Jiang, Xuanang Li, Xiaoran Shang, Guancheng Wan, Hengli Li, <strong>Mengting Li</strong>, Zhaolu Kang, Xinfeng Li, Ying Nian Wu</dd>
<dd>Submitted to ACL Rolling Review, 2025</dd>
</dl>


<hr>





<dl>
  <dd><a href=""><strong> 
Attention-Based BiLSTM Framework for Speech Emotion Recognition Using MFCCs and Interpretability via NAOPC and Attention Weights
</strong></a></dd>
<dd><strong>Mengting Li</strong></dd>
<dd> Submitted to Interspeech 2026</dd>
</dl>


<hr>


<dl>
  <dd><a href=""><strong> 
AI-Driven Analysis of Mental Health Outcomes Using Cedars-Sinai Patient Data
</strong></a></dd>
<dd><strong>Mengting Li</strong></dd>
<dd> Internal research report at Cedars-Sinai Clinical Research Team, 2025</dd>
</dl>


<hr>







<br/>

# 🎖 Scholarships and Honors

- *2025* <a href="https://ucla.academicworks.com/opportunities/119805">**S & S Scholarship Fund** </a>  *UCLA*



- *2024* <a href="https://ucla.academicworks.com/opportunities/119805">**S & S Scholarship Fund** </a>  *UCLA*








<br/>

# 📖 Education

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2022.09 - Now</strong><br/>
      Undergraduate, Statistics & Data Science, University of California, Los Angeles (UCLA)
    </div>
  </div>
  <div class="education-logo">
    <img src="../images/UCLA.png" alt="UCLA Logo" />
  </div>
</div>


# 💼 Experience



<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
    <a href="https://web.cs.ucla.edu/~kwchang/">UCLA NLP Group</a>, University of California, Los Angeles
    </div>
    <div class="experience-role">Research Assistant, 2025</div>
    <div class="experience-topics">Topics: LLM, LLM Agents</div>
  </div>
  <div class="experience-logo">
    <img src="../images/uclanlp.png" alt="ScAi Logo" />
  </div>
</div>




<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://www.cedars-sinai.org/home.html">Cedars-Sinai Medical Center</a>, Los Angeles
    </div>
    <div class="experience-role">Research Assistant, 2024-2025</div>
    <div class="experience-topics">Topics: AI for Healthcare</div>
  </div>
  <div class="experience-logo">
    <img src="../images/Cedars.png" alt="Cedars-Sinai Logo" />
  </div>
</div>
  <div class="experience-card">
    <div class="experience-info">
      <div class="experience-title">
        <a href="http://www.stat.ucla.edu/~ywu/research.html">Ying Nian Wu's Lab</a>, University of California, Los Angeles
      </div>
      <div class="experience-role">Research Assistant, 2024-2025</div>
      <div class="experience-topics">Topics: LLM, LLM Agents, Graph Learning</div>
    </div>
  <div class="experience-logo">
    <img src="../images/UCLA.png" alt="UCLA Logo" />
  </div>
  </div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://www.mit.edu/">Massachusetts Institute of Technology (MIT)</a>, Cambridge, Massachusetts
    </div>
    <div class="experience-role">Machine Learning Researcher (Intern), 2023.07 - 2023.08</div>
    <div class="experience-topics">Topics: RF, LR, XGBoost; Benchmarking</div>
    <div class="experience-topics">Highlights: Directed a 4-person data science team</div>
  </div>
  <div class="experience-logo">
    <img src="../images/MIT.png" alt="MIT Logo" />
  </div>
</div>

<dl><a href="https://clustrmaps.com/site/1bxa7" title="Visit tracker"><img src="//clustrmaps.com/map_v2.png?cl=080808&w=400&t=n&d=3d-gAqSb6Wx-DoL_BIvviv0g9ivHnOPl9-3M98ywjqw&co=ffffff&ct=808080" /></a></dl>



<!-- 
# 🐰 Miscellaneous

### 📖 Poems that Inspire Me

- **白鹭立雪，愚者看鹭，聪者观雪，智者见白** —— A white egret stands in the snow. The foolish see only the egret, the wise observe the snow, and the enlightened perceive the whiteness.
- **世界不黑也不白, 而是一道精致的灰** —— The world is neither black nor white, but a delicate shade of gray.
- **风吹到哪页，读哪页** —— The wind blows to which page, read which page.  -->
