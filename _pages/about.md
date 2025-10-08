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


My name is Guancheng Wan (万冠呈) <span class="pronunciation" style="cursor: pointer;" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'; this.querySelector('.toggle-symbol').textContent = this.nextElementSibling.style.display === 'block' ? '▼' : '►';"><span class="toggle-symbol" style="margin-right: 5px;">►</span><span style="color: gray;">How to pronounce?</span></span>
<span style="display: none;">My name is pronounced as "Gwan-chung Wan". The "Gwan" rhymes with "man", and "chung" sounds like "chung" in "chunk".</span>, a CS Ph.D. student at University of California, Los Angeles ([UCLA](https://www.ucla.edu/)), supervised by [Yizhou Sun](https://scholar.google.com/citations?user=TQgOjK0AAAAJ) and [Wei Wang](https://scholar.google.com/citations?user=UedS9LQAAAAJ) (IEEE/ACM Fellow). I obtained my B.S. degree at [Wuhan University](https://www.whu.edu.cn/), advised by [Mang Ye](https://jszy.whu.edu.cn/yemang/zh_CN/index.htm), [Bo Du](https://cs.whu.edu.cn/info/1019/2892.htm) and [Wenke Huang](https://wenkehuang.github.io/). 

I am open to any research collaboration and internship, with a great record of cooperating and mentoring. 🥳 Feel free to contact me via <a href="mailto:gcwan03@ucla.edu">Email</a> or <a href="https://guanchengwan.github.io/images/wechat.png">WeChat</a>.


<div style="text-align: left; margin: 20px 0;">
  <img src="../images/sign.png" alt="Signature" style="max-width: 150px; height: auto;">
</div>


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

<dt style="text-align: center; margin: 0; padding: 0;">
  <img src="../images/research.png" style="display: block; max-width: 700px; width: 100%; height: auto; margin: 0 auto;">
</dt>

I am passionate about modeling the relationships among all points (*e.g.*, nodes, tokens, or agents). My current research interests focus on three key areas:

a) (Multimodal) Large Language Models (MLLM), Large Reasoning Models, LLM-based Multi-Agent System

b) AI for Science: Biotechnology, Physics and Chemistry...

c) Trustworthy AI:  Federated (Graph) Learning, MLLM Safety and Hallucination 



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








# 📃 Selected Publications ([Full List](https://scholar.google.com/citations?user=pB8zP9UAAAAJ))

**&dagger; Equal Contribution**   

<div style="text-align: left; margin: 20px 0; font-size: 1.5em; color: #666;">
2025 
</div>

<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/FedTGE.png">
<span class="conference-label">ICLR 2025</span>
</dt>
  <dd><a href="https://openreview.net/forum?id=5Jc7r5aqHJ"><strong>	
Energy-based Backdoor Defense Against Federated Graph Learning
</strong></a></dd>
<dd><strong><strong>Guancheng Wan</strong>&dagger;</strong>, Zitong Shi&dagger;, Wenke Huang&dagger;, Guibin Zhang, Dacheng Tao, Mang Ye</dd>
<dd> <strong class="co-first"><i>Oral Presentation (Top 1.8%)</i></strong> in International Conference on Learning Representations (<strong>ICLR</strong>), 2025</dd>
</dl>

<hr>


<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/HYPERION.png">
<span class="conference-label">NeurIPS 2025</span>
</dt>
  <dd><a href=""><strong>HYPERION: Fine-Grained Hypersphere Alignment for Robust Federated Graph Learning</strong></a></dd>
  <dd><strong>Guancheng Wan&dagger;</strong>, Xiaoran Shang, Guibin Zhang, Jinhe Bi, Yuxin Wu, Liangtao Zheng, Xin Lin, Yue Liu, Yanbiao Ma, Wenke Huang, Bo Du</dd>
  <dd><strong class="co-first"><i>Spotlight Presentation (Top 3.1%)</i></strong> in Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025</dd>
</dl>


<hr>

<dl>
  <dt><img align="left" width="100"
  hspace="10" wspace="20" src="../images/GREAT.png">
  <span class="conference-label">ICML 2025</span>
</dt>
  <dd><a href=""><strong>Rethink GraphODE Generalization within Coupled Dynamical System</strong></a></dd>
<dd><strong>Guancheng Wan</strong>, Zijie Huang, Wanjia Zhao, Xiao Luo, Yizhou Sun, Wei Wang</dd>
<dd>  <strong class="co-first"><i>Spotlight Presentation (Top 2.6%)</i></strong> in International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>



<hr>
<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/OASIS.png">
<span class="conference-label">NeurIPS 2025</span>
</dt>
  <dd><a href=""><strong>OASIS: One-Shot Federated Graph Learning via Wasserstein Assisted Knowledge Integration</strong></a></dd>
  <dd><strong>Guancheng Wan&dagger;</strong>, Jiaru Qian, Wenke Huang, Qilin Xu, Xianda Guo, Boheng Li, Guibin Zhang, Bo Du, Mang Ye</dd>
  <dd>Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025</dd>
</dl>


<hr>




<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/LoRASculpt.png">
<span class="conference-label">CVPR 2025</span>
</dt>
  <dd><a href=""><strong>LoRASculpt: Sculpting LoRA for Harmonizing General and Specialized Knowledge in Multimodal Large Language Models</strong></a></dd>
  <dd>Jian Liang&dagger;, Wenke Huang&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Qu Yang, Mang Ye</dd>
  <dd><strong class="co-first"><i>Oral Presentation (Top 3.3%)</i></strong> in Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2025</dd>
</dl>

<hr>


<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/FedSPA.png">
<span class="conference-label">CVPR 2025</span>
</dt>
  <dd><a href=""><strong>FedSPA: Generalizable Federated Graph Learning under Homophily Heterogeneity</strong></a></dd>
  <dd>Zihan Tan&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Wenke Huang, Guibin Zhang, He Li, Carl Yang, Mang Ye</dd>
  <dd>Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2025</dd>
</dl>

<hr>



<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/GMemory.png">
<span class="conference-label">NeurIPS 2025</span>
</dt>
  <dd><a href=""><strong>G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems</strong></a></dd>
  <dd>Guibin Zhang, Muxin Fu, <strong>Guancheng Wan</strong>, Miao Yu, Kun Wang, Shuicheng Yan</dd>
  <dd><strong class="co-first"><i>Spotlight Presentation (Top 3.1%)</i></strong> in Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025</dd>
</dl>

<hr>


<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/EARTH.png">
<span class="conference-label">ICML 2025</span>
</dt>
  <dd><a href="https://arxiv.org/abs/2410.00049"><strong>Epidemiology-Aware Neural ODE with Continuous Disease Transmission Graph</strong></a></dd>
<dd><strong>Guancheng Wan</strong>, Zewen Liu, Xiaojun Shan, Max S.Y. Lau, B. Aditya Prakash, Wei Jin</dd>
<dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>


<hr>




<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/EMOE.png">
<span class="conference-label">CVPR 2025</span>
</dt>
  <dd><a href=""><strong>EMOE: Modality-Specific Enhanced Dynamic Emotion Experts</strong></a></dd>
  <dd>Yiyang Fang&dagger;, Wenke Huang&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Kehua Su, Mang Ye</dd>
  <dd>Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2025</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/GHOST.png">
  <span class="conference-label">ICML 2025</span>
  </dt>
  <dd><a href=""><strong>GHOST: Generalizable One-Shot Federated Graph Learning with Proxy-Based Topology Knowledge Retention</strong></a></dd>
  <dd>Jiaru Qian&dagger;, <strong>Guancheng Wan</strong>&dagger; <span class="co-first">(co-first)</span>, Wenke Huang, Guibin Zhang, Yuxin Wu, Bo Du, Mang Ye</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/GSafeguard.png">
  <span class="conference-label">ACL 2025 Main</span>
  </dt>
  <dd><a href=""><strong>G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems</strong></a></dd>
  <dd>Shilong Wang, Guibin Zhang, Miao Yu, <strong>Guancheng Wan</strong>, Fanci Meng, Chongye Guo, Kun Wang, Yang Wang</dd>
  <dd>Annual Meeting of the Association for Computational Linguistics (<strong>ACL</strong>), 2025</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/EAGLES.png">
  <span class="conference-label">ICML 2025</span>
  </dt>
  <dd><a href=""><strong>EAGLES: Towards Effective, Efficient, and Economical Federated Graph Learning via Unified Sparsification</strong></a></dd>
  <dd>Zitong Shi&dagger;, <strong>Guancheng Wan</strong>&dagger; <span class="co-first">(co-first)</span>, Guibin Zhang, Wenke Huang, He Li, Carl Yang, Mang Ye</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>




<hr>


<dl>
  <dt><img align="left" width="100"
  hspace="10" wspace="20" src="../images/MOTION.png">
  <span class="conference-label">NeurIPS 2025</span>
  </dt>
  <dd><a href=""><strong>MOTION: Multi-Sculpt Evolutionary Coarsening for Federated Continual Graph Learning</strong></a></dd>
  <dd><strong>Guancheng Wan&dagger;</strong>, Fengyuan Ran, Ruikang Zhang, Wenke Huang, Xuankun Rong, Guibin Zhang, Yuxin Wu, Bo Du, Mang Ye</dd>
  <dd>Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025</dd>
</dl>


<hr>


<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/Gdesigner.png">
  <span class="conference-label">ICML 2025</span>
  </dt>
  <dd><a href=""><strong>G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks</strong></a></dd>
  <dd>Guibin Zhang, Yanwei Yue, Xiangguo Sun, <strong>Guancheng Wan</strong>, Miao Yu, Junfeng Fang, Kun Wang, Tianlong Chen, Dawei Cheng</dd>
  <dd> <strong class="co-first"><i>Spotlight Presentation (Top 2.6%)</i></strong> in International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/BeConfident.png">
  <span class="conference-label">ICML 2025</span>
  </dt>
  <dd><a href=""><strong>Be Confident: Uncovering Overfitting in MLLM Multi-Task Tuning</strong></a></dd>
  <dd>Wenke Huang, Jian Liang, <strong>Guancheng Wan</strong>, Didi Zhu, He Li, Jiawei Shao, Mang Ye, Bo Du, Dacheng Tao</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>

<hr>


<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/agentprune.png">
  <span class="conference-label">ICLR 2025</span>
  </dt>
  <dd><a href="https://openreview.net/forum?id=LkzuPorQ5L"><strong>	
Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems
</strong></a></dd>
  <dd>Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, <strong>Guancheng Wan</strong>, Kun Wang, Dawei Cheng, Jeffrey Xu Yu, Tianlong Chen</dd>
  <dd>International Conference on Learning Representations (<strong>ICLR</strong>), 2025</dd>
</dl>

<hr>

<!-- 
<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/FedPHA.png">
<span class="conference-label">ICML 2025</span>
</dt>
  <dd><a href=""><strong>FedPHA: Federated Prompt Learning for Heterogeneous Client Adaptation</strong></a></dd>
  <dd>Chengying Fang&dagger;, Wenke Huang&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Yihao Yang, Mang Ye</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>

<hr> -->


<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/LearnFromDownstream.png">
  <span class="conference-label">ICML 2025</span>
  </dt>
  <dd><a href=""><strong>Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning</strong></a></dd>
  <dd>Wenke Huang, Jian Liang, Zekun Shi, Didi Zhu, <strong>Guancheng Wan</strong>, He Li, Bo Du, Dacheng Tao, Mang Ye</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>



<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/FedPrompt.png">
  <span class="conference-label">IJCAI 2025</span>
  </dt>
  <dd><a href=""><strong>An Empirical Study of Federated Prompt Learning for Vision Language Model</strong></a></dd>
  <dd>Zhihao Wang, Wenke Huang, Tian Chen, Zekun Shi, <strong>Guancheng Wan</strong>, Yu Qiao, Bin Yang, Jian Wang, Bing Li, Mang Ye</dd>
  <dd>The 34th International Joint Conference on Artificial Intelligence (<strong>IJCAI</strong>), 2025</dd>
</dl>

<!-- 
<hr>

<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/FedDisentangledTuning.png">
<span class="conference-label">ICML 2025</span>
</dt>
  <dd><a href=""><strong>Federated Disentangled Tuning with Textual Prior Decoupling and Visual Dynamic Adaptation</strong></a></dd>
  <dd>Yihao Yang&dagger;, Wenke Huang&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Bin Yang, Mang Ye</dd>
  <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl> -->

<hr>

<dl>
  <dt><img align="left" width="100"
hspace="10" wspace="20" src="../images/FedICU.jpg"> <span class="conference-label">ICML 2025</span>
</dt>
  <dd><a href=""><strong>Splitting with Importance-aware Updating for Heterogeneous Federated Learning with Large Language Models</strong></a></dd>
<dd>Yangxu Liao&dagger;, Wenke Huang&dagger;, <strong>Guancheng Wan&dagger;</strong> <span class="co-first">(co-first)</span>, Jian Liang, Bin Yang, Mang Ye</dd>
<dd>International Conference on Machine Learning (<strong>ICML</strong>), 2025</dd>
</dl>
<hr>


<br>

<div style="text-align: left; margin: 20px 0; font-size: 1.5em; color: #666;">
2024
</div>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/S3GCL_ICML24.png">
  <span class="conference-label">ICML 2024</span>
  </dt>
  <dd><a href="https://proceedings.mlr.press/v235/wan24g.html"><strong>S3GCL: Spectral, Swift, Spatial Graph Contrastive Learning
</strong></a></dd>
  <dd><strong>Guancheng Wan</strong>, Yijun Tian, Wenke Huang, Nitesh V Chawla, Mang Ye</dd>
    <dd>International Conference on Machine Learning (<strong>ICML</strong>), 2024 </dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/FedSSP.png">
  <span class="conference-label">NeurIPS 2024</span>
  </dt>
  <dd><a href="https://arxiv.org/pdf/2410.20105"><strong>FedSSP: Federated Graph Learning with Spectral Knowledge and Personalized Preference</strong></a></dd>
  <dd>Zihan Tan&dagger;, <strong>Guancheng Wan&dagger; </strong><span class="co-first">(co-first)</span>, Wenke Huang&dagger;, Mang Ye</dd>
  <dd>Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024</dd>
</dl>

<hr>
<!-- 
<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/FDCR.png">
  <span class="conference-label">NeurIPS 2024</span>
  </dt>
  <dd><a href=""><strong>	
Parameter Disparities Dissection for Backdoor Defense in Heterogeneous Federated Learning</strong></a></dd>
  <dd>Wenke Huang, Mang Ye, Zekun Shi, <strong>Guancheng Wan</strong>, He Li, Bo Du
  </dd>
  <dd>Annual Conference on Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024</dd>
</dl>

<hr> -->

<dl>
  <dt><img align="left"  width="100"
  wspace="20" hspace="10" src="../images/fggp.png">
  <span class="conference-label">AAAI 2024</span>
  </dt>
  <dd ><a href="https://ojs.aaai.org/index.php/AAAI/article/view/29468"><strong> Federated Graph Learning under Domain Shift with Generalizable Prototypes</strong></a></dd>
  <dd><strong>Guancheng Wan</strong>, Wenke Huang, Mang Ye</dd>
    <dd> Annual AAAI Conference on Artificial Intelligence (<strong>AAAI</strong>), 2024</dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/episurvey.png">
  <span class="conference-label">KDD 2024</span>
  </dt>
  <dd><a href="https://dl.acm.org/doi/pdf/10.1145/3637528.3671455"><strong>A Review of Graph Neural Networks in Epidemic Modeling</strong></a></dd>
  <dd>Zewen Liu&dagger;, <strong>Guancheng Wan&dagger; </strong><span class="co-first">(co-first)</span>, B. Aditya Prakash, Max S. Y. Lau, Wei Jin</dd>
    <dd>ACM SIGKDD Conference on Knowledge Discovery and Data Mining (<strong>KDD</strong>), 2024</dd>
    <dd><a href="https://github.com/Emory-Melody/awesome-epidemic-modeling-papers">Project Page</a></dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10"   wspace="20" src="../images/fgssl.png">
  <span class="conference-label">IJCAI 2023</span>
  </dt>
  <dd><a href="https://arxiv.org/pdf/2406.18937"><strong>Federated Graph Semantic and Structural Learning</strong></a></dd>
  <dd>Wenke Huang&dagger;, <strong>Guancheng Wan&dagger; </strong><span class="co-first">(co-first)</span>, Mang Ye, Bo Du</dd>
  <dd> International Joint Conference on Artificial Intelligence (<strong>IJCAI</strong>), 2023  </dd>
</dl>

<hr>

<dl>
  <dt><img align="left"  width="100"
  hspace="10" wspace="20" src="../images/flsurvey.png">
  <span class="conference-label">TPAMI 2024</span>
  </dt>
  <dd><a href="https://arxiv.org/abs/2311.06750"><strong>Federated Learning for Generalization, Robustness, Fairness: A Survey and Benchmark</strong></a></dd>
  <dd>Wenke Huang, Mang Ye, Zekun Shi, <strong>Guancheng Wan</strong>, He Li, Bo Du,  Qiang Yang
  </dd>
    <dd>IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024</dd>
    <dd><a href="https://github.com/WenkeHuang/MarsFL">Project Page</a></dd>
</dl>



<br>


# 🔬 Survey and Benchmark

- **Protein Large Language Models: A Comprehensive Survey, EMNLP 2025 Findings** 

- **Keeping Yourself is Important in Downstream Tuning Multimodal Large Language Model**

- **A Comprehensive Survey in LLM (-Agent) Full Stack Safety: Data, Training and Deployment**

- **From Web Search towards Agentic Deep ReSearch: Incentivizing Search with Reasoning Agents**

- **A Comprehensive Survey of Evaluating Multimodal Foundation Models: Hierarchical Perspective and Extensive Applications**

- **A Comprehensive Survey on Scientific Large Language Models in Physics**

- **FD-Bench: A Modular and Fair Benchmark for Data-driven Fluid Simulation**






# 🎡 Service

<div class="service-section">
  <h3>Program Chair</h3>
  <ul class="service-list">
    <li><a href="https://fedkdd.github.io/fedkdd2025/">FedKDD 2025 Workshop@KDD 2025</a></li>
  </ul>
</div>

<div class="service-section">
  <h3>Conference Committee Member</h3>
  <ul class="service-list">
    <li>Reviewer for ICML, ICLR, NeurIPS, AISTATS</li>
    <li>Reviewer for CVPR, ICCV, ECCV</li>
    <li>Reviewer for ARR, ACL, EMNLP, NAACL</li>
    <li>Reviewer for AAAI, IJCAI, ACM MM</li>

  </ul>
</div>

<div class="service-section">
  <h3>Journal Reviewer</h3>
  <ul class="service-list">
    <li>IEEE TIFS, TIP, TKDE, TNNLS</li>
    <li>ACM TKDD</li>
    <li>Pattern Recognition (PR)</li>
    <li>Data-centric Machine Learning Research (DMLR)</li>
  </ul>
</div>

<!-- - Reviewer for Data-centric Machine Learning Research (DMLR) -->


<br/>

# 🎖 Scholarships and Honors

- *2024.11* <a href="https://mp.weixin.qq.com/s/aS639YfEZLi2Y457L5XjUg">**Lei Jun Excellence Scholarship** </a>(**<u>雷军卓越奖学金</u>**) **~100k** (The **<u>Highest</u>** Scholarship at Wuhan University, **<u>Top-4</u>** among All Undergraduates, Award Rate ~ **0.01%**)  *Wuhan University*

- *2023.09* **National Scholarship** **(<u>Twice</u>)** (**<u>国家奖学金</u>**) (Award Rate: <strong>0.2% nation-wide</strong>) *Ministry of Education, China* 

- *2022.09* **National Scholarship** (**<u>国家奖学金</u>**) (Award Rate: <strong>0.2% nation-wide</strong>) *Ministry of Education, China* 

- *2025.03* <a href="https://mp.weixin.qq.com/s/1quPOGcxbMkfMFgkl8tFKQ">**Luo Jia Role model** </a>(榜样珞珈年度人物) (10 Students school-wide)  *Wuhan University*

- *2024.11* **InnoStar Undergraduate Innovation Achievement Award** (英诺大学生创新成果 特等奖) ~30k (**Only 2** Students school-wide) *Wuhan University*

- *2024.10* **Luojia Undergraduate Innovation Research Fund** (首批珞珈本科生研究基金) ~50k (4 Students department-wide)  *Wuhan University*

- *2024.06* **Lei Jun Computer Innovation and Development Fund** and  **Research Fund** (雷军创新发展基金、雷军研究基金) (3 Students department-wide)  *Wuhan University*

<!-- - *2024.06* <a href="https://scholarship2024.sensetime.com/cn/">**SenseTime Scholarship**</a> (商汤奖学金) ~20k (**25 Students nation-wide**) *SenseTime* -->

- *2024.04* <a href="https://mp.weixin.qq.com/s/zdx8hH8-g0FScgZvkYQRnw">**CS Pioneer**</a> (计科先锋年度人物) (10 Students department-wide)  *Wuhan University*

- *2023.10* **CCF (China Computer Federation) Elite Collegiate Award** (CCF优秀大学生) (102 Students nation-wide) *China Computer Federation*

- *2023.10* **Pacemaker to Merit Student** (三好学生标兵) (Award Rate ~ <strong>0.1%</strong>) *Wuhan University*


<br/>

# 📖 Education

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2025.09 - Now</strong><br/>
      PhD, Computer Science, University of California, Los Angeles (UCLA)
    </div>
  </div>
  <div class="education-logo">
    <img src="../images/UCLA.png" alt="UCLA Logo" />
  </div>
</div>

<div class="education-card">
  <div class="education-info">
    <div class="education-title">
      <strong>2021.09 - 2025.06</strong><br/>
      Bachelor, School of Computer Science, Wuhan University
    </div>
  </div>
  <div class="education-logo">
    <img src="../images/WHU.jpeg" alt="Wuhan University Logo" />
  </div>
</div>


# 💼 Experience

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://www.princeton.edu/">Princeton University</a>
    </div>
    <div class="experience-role">Research Internship, 2025</div>
    <div class="experience-topics">Topics: AI for Science</div>
  </div>
  <div class="experience-logo">
    <img src="../images/princeton.png" alt="Princeton Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://sail.sea.com/">Sea AI Lab, Singapore</a>
    </div>
    <div class="experience-role">Internship, Associate member, 2025</div>
    <div class="experience-topics">Topics: (M)LLM, GUI Agent</div>
  </div>
  <div class="experience-logo">
    <img src="../images/sea.png" alt="Sea AI Lab Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://ucla-dm.github.io/DM_website/">UCLA Data Mining Lab</a> & <a href="http://web.cs.ucla.edu/~weiwang/">ScAI Lab</a>, University of California, Los Angeles
    </div>
    <div class="experience-role">Research Internship, 2024-2025</div>
    <div class="experience-topics">Topics: Ai4Science, Dynamic System, Graph Neural ODE</div>
  </div>
  <div class="experience-logo">
    <img src="../images/UCLA.png" alt="UCLA Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://www.cs.emory.edu/~wjin30/">Melody Lab</a>, Emory University
    </div>
    <div class="experience-role">Research Assistant, 2024</div>
    <div class="experience-topics">Topics: Ai4Science, Epidemiology, Graph Learning</div>
  </div>
  <div class="experience-logo">
    <img src="../images/emory.png" alt="Emory Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://adityalab.cc.gatech.edu/">Aditya Lab</a>, Georgia Institute of Technology
    </div>
    <div class="experience-role">Research Assistant, 2024</div>
    <div class="experience-topics">Topics: Ai4Science, Epidemiology, Graph Learning</div>
  </div>
  <div class="experience-logo">
    <img src="../images/gatech.png" alt="Georgia Tech Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://lucyinstitute.nd.edu/centers-and-labs/data-inference-analytics-and-learning-dial-lab/">DIAL Lab</a>, University of Notre Dame
    </div>
    <div class="experience-role">Research Internship, 2023</div>
    <div class="experience-topics">Topics: Inference Acceleration, Heterophilic Graph, Unsupervised Learning</div>
  </div>
  <div class="experience-logo">
    <img src="../images/ND.png" alt="Notre Dame Logo" />
  </div>
</div>

<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://marswhu.github.io/">MARS lab</a>, Wuhan University
    </div>
    <div class="experience-role">Research Assistant, 2023-2025</div>
    <div class="experience-topics">Topics: Robustness, Backdoor Attack, Graph Learning, Domain Generalization, Federated Learning</div>
  </div>
  <div class="experience-logo">
    <img src="../images/WHU.jpeg" alt="WHU Logo" />
  </div>
</div>


<div class="experience-card">
  <div class="experience-info">
    <div class="experience-title">
      <a href="https://sigma.whu.edu.cn/">SIGMA lab</a>, Wuhan University
    </div>
    <div class="experience-role">Research Assistant, 2023-2025</div>
    <div class="experience-topics">Topics: Robustness, Backdoor Attack, Graph Learning, Domain Generalization, Federated Learning</div>
  </div>
  <div class="experience-logo">
    <img src="../images/sigma.png" alt="WHU Logo" />
  </div>
</div>


<dl><a href="https://clustrmaps.com/site/1bxa7" title="Visit tracker"><img src="//clustrmaps.com/map_v2.png?cl=080808&w=400&t=n&d=3d-gAqSb6Wx-DoL_BIvviv0g9ivHnOPl9-3M98ywjqw&co=ffffff&ct=808080" /></a></dl>




# 🏀 Miscellaneous


### 📖 Poems that Inspire Me

- **白鹭立雪，愚者看鹭，聪者观雪，智者见白** —— A white egret stands in the snow. The foolish see only the egret, the wise observe the snow, and the enlightened perceive the whiteness.
- **世界不黑也不白, 而是一道精致的灰** —— The world is neither black nor white, but a delicate shade of gray.
- **风吹到哪页，读哪页** —— The wind blows to which page, read which page.

### 🎤 Favorite Hip-Hop Artists

- **GALI** - Chinese rapper known for his unique flow and profound lyrics
- **G-BLOCK** - Hip-hop collective consisting of GAI, 盛宇, 功夫胖, and 刘聪, representing the Southwest China rap scene
- **Travis Scott** - American rapper and producer famous for his influential Astroworld album


### 💬 Talks and Shares

- [📺 泛化图学习与本科生科研经历分享](https://www.bilibili.com/video/BV1gZ42177VL/?spm_id_from=333.337.search-card.all.click&vd_source=0b7a3cc3d3ec288abaca83b9a7e036af)

### 🎓 Undergraduate Research Resources

- [📄 Undergraduate research resource and enrollment process](https://zxeupbuzh9y.feishu.cn/docx/ZDEsdpZtPosRWOxcBnkcF8Hknkd)