# superMAN

# Never fear, superMAN is here! 🦸‍♂️

## Inspiration ✨
The inspiration for superMAN arose from the desire to enhance the command-line experience for users, especially when navigating Linux commands. Many users find traditional MAN pages overwhelming, and searching the internet for the right commands can be time-consuming. Whether its finding one of the dozens of flags for ls, determining the exact git commands to fix your broken repository, or simply learning more about bash, superMAN aims to bridge knowledge gaps by allowing users to describe tasks in plain language and receive instant, precise terminal commands. Not only will users be able to run generated commands with one button press, but they can also get explanations directly in their terminal, making it easier to learn and grow their skills as they work. By leveraging open source AI technology, superMAN transforms the command line into a more accessible and empowering tool for everyone. SuperMAN and its underlying models collect no data whatsoever and do not use user prompts for model training, allowing complete peace of mind for privacy.

## What it does ⚙️
At its core, superMAN is designed to make command-line usage more intuitive and user-friendly. Here’s what it fundamentally does:
- ***Natural Language Processing***: Users can describe their desired tasks or commands in plain language rather than needing to know the exact syntax or command structure. 
- ***Command Generation***: superMAN interprets the user's input and generates the corresponding terminal commands, streamlining the process of executing tasks.
- ***Learning and Explanation***: Along with providing the commands, superMAN can offer explanations and descriptions of what each command does, allowing users to learn and understand the underlying concepts as they work.
- ***Accessibility***: It removes the barriers associated with traditional MAN pages and command-line usage, making it easier for both novice and experienced users to interact with the terminal. It is currently accessible to any student logged onto the UTCS lab machines.
- ***Efficiency***: By reducing the time spent searching for commands or understanding syntax, superMAN helps users accomplish their tasks more quickly and efficiently, enhancing overall productivity.
- ***Privacy***: Unlike for-profit models and companies offering similar services, superMAN uses open source models as its base and collects no user data. This allows for full privacy of all queries and responses through this tool.

## How we built it 🤓
- UI: We got creative here- the entire UI is inside of the terminal window using the colorama python package and ASCII art.
- Client shell: A python script that makes requests to our cloudflare server, sending prompts and getting back model output.
- DNS/Port Forwarding: Cloudfare Service (allows access to users outside local network and provides free-tier basic protection)
- LLM inference acceleration: IPEX-LLM( Intel® Extension for PyTorch* Large Language Models) helped superMAN run faster and more efficiently by optimizing model performance on Intel hardware. Its tailored optimizations sped up response times and reduced resource usage, allowing superMAN to deliver quick, accurate, and seamless command-line assistance. The cherry on top is that it had integration compatibility with Ollama, a service that we have familiarity with.
- API Service: Ollama Serve allowed us to access Ollama through a local "REST API" call, exposing its port to our Cloudflare server.
- Model manager: Ollama is an open-source platform that allowed us to simultaneously run multiple customized LLMs locally on the AIPC.
- Base AI model: LLaMA3.2. After iterative testing of LLMs of all different sizes and specialties, we found LLaMA3.2 to be the most consistent and accurate model for our task.
- Hardware: Intel AI-PC. This hardware enabled superMAN to run AI tasks quickly and securely on local machines. With their high processing power, the Intel AIPC handled intensive AI workloads with low latency, ensuring a responsive user experience. Running locally also enhanced security, as all data stayed on the user's device, protecting privacy and making command-line interactions fast, private, and efficient.

## Challenges we ran into 🏔️
- Selecting a Model: Choosing the right language model was crucial for accuracy and performance. We had to balance model complexity with resource efficiency to ensure real-time responses. We actually ran a small experiment on the AIPC to find out which model used the Intel GPU most efficiently and gave us back the fastest and most accurate response!
- Running Code on the GPU, Not CPU: Transitioning from CPU to GPU was a challenge, but IPEX-LLM provided optimizations that leveraged the GPU on Intel hardware effectively, enabling faster processing and lower latency.
- Handling Non-Local Requests to Ollama: Working with non-local requests involved setting up ports, configuring hosts, and learning basic networking principles. This was essential for external connections and handling user interactions reliably. We were able to leverage Cloudflare services to allow users around the world to use SuperMAN.
- Building Familiarity with Intel Tools: There was a learning curve with Intel tools, but it was exciting to explore how Intel's AI tools and AIPCs enhanced performance. The learning paths we were provided with taught us lot about the inner workings of Intel's software tools and helped us select IPEX-LLM for our project. This tool was critical in optimizing superMAN’s speed and efficiency. 
- Setting Up DDoS Protection and Security: To protect superMAN, we implemented DDoS protection with Cloudflare and other security measures. Ensuring robust security was essential for protecting user data and maintaining service reliability.

## Accomplishments that we're proud of 🏆
Having a functional MVP!
Optimizing our project utilizing the full capabilities of an Intel AIPC.
Making something actually accessible and free for all UTCS students to use during competition.
Learning a lot really fast in a really short amount of time.

## What we learned ✏️
- Exploring the Intel AI Ecosystem: Diving into Intel's AI ecosystem was an eye-opener. We learned how Intel’s AIPCs, IPEX-LLM, and associated tools work together to create a powerful foundation for AI applications. The compatibility of these tools allowed us to streamline our development, optimize for hardware, and see the benefits of hardware-software synergy firsthand. It was inspiring to see how each component—from hardware to acceleration software—fit into a cohesive, high-performance AI solution.
- Networking and Security Fundamentals: Setting up network configurations for non-local requests was a valuable experience in networking essentials, from port management to host setup. Implementing security measures like Cloudflare’s DDoS protection taught us the importance of safeguarding user data and service reliability. These skills are crucial when scaling any web-based tool, especially one that processes sensitive information.
- Rapid Prototyping and Adaptability: Working under a tight deadline underscored the importance of agile development and adaptability. We had to make quick decisions, prioritize features, and problem-solve on the fly. This experience not only strengthened our technical skills but also reinforced the value of teamwork, flexibility, and iterative improvements in bringing an idea from concept to MVP.
- The Power of On-Device AI for Privacy and Speed: Running superMAN locally on the Intel AIPC allowed us to keep all data processing on-device, enhancing both privacy and speed. This experience highlighted the value of on-device AI solutions, especially in applications where user data security and low-latency interactions are essential. We saw how edge computing can make powerful tools accessible, secure, and efficient.

## What's next for SuperMAN
Although it was really cool and really fun seeing how the Intel AIPC could run the model so efficiently, after this competition we will need to find an alternative platform to run the IPEX-LLM LLaMA3.2 model. An Intel Cloud server can probably integrate the best with IPEX-LLM to keep the back-end running for anyone to use.

### Special thanks to Intel for providing the AI-PC and helpful resources! 
