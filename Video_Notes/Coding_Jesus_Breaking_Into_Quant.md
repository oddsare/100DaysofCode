# Coding Jesus: Breaking Into Quant (video notes)

> **AI generated.** Notes written by AI (Claude) from the video's transcript, to come back to later. Words marked *(unsure)* were garbled in the transcript, so they're my best guess.

## What the video is

- **Who:** CJ, the "Coding Jesus" YouTube channel. He talks about getting jobs in **quant trading** (building trading systems for hedge funds and trading firms).
- **His main point:** people who can't get in after years usually don't have a "job market problem", they have a "guided progress problem". Degrees and certificates matter less than **what you've built and can explain**.
- **Heads up:** a big part of the video is an ad. It sells his paid **90-day Quant Accelerator** program (from GetCracked *(unsure of exact name)*) and a sponsored cloud server company. His claims (like "there's no job market problem") are his opinion, not facts he backs with numbers.

## The big idea: build a project that makes you stand out

- Copying a popular YouTube project doesn't help, because thousands of people have the same one.
- Pick a project that shows the **skills the job needs**. It doesn't even have to be about finance: he hired someone who built a **Pokémon trading card Discord bot**, because that person could explain it deeply.
- A firm's recruiter contacted one of his students **because of a project** the student posted.

## The 4 questions you must be able to answer about any project

1. What did you build?
2. Why did you build it?
3. What mistakes did you make while building it?
4. If you could go back, what would you do differently?

He says most people fail on **3 and 4**, because they only want to talk about strengths. Interviewers want to hear about **trade-offs** and **what you'd improve**, because that's what the job is.

*For me:* these work for my 100 Days projects too. For example, Blackjack: the Aces bug (same Ace dropping twice), and what I'd do differently (one function to work out the total).

## What quant firms want you to know (decoded)

This is the advanced end. Most of it is **C++ and Linux**, not Python.

| Topic | What it means in plain words |
| --- | --- |
| **Modern C++** | The language most trading systems are written in, because it's very fast |
| Type safety, ownership, RAII | Rules that stop memory bugs: who "owns" each piece of data, and cleaning up automatically when it's done |
| `std::variant`, `std::byte`, `std::hive` | Newer C++ building blocks. He wants you to know **why** you picked one over another, not just that it exists |
| **Linux** | The operating system their servers run. You should be comfortable using it |
| **Networking / sockets** | How one computer sends data to another (socket, bind, listen, accept, send, receive) |
| **TCP** | The common way to send data reliably over a network |
| Event loops (**epoll** *(unsure)*) | One program handling lots of connections at once without waiting on each one |
| gRPC / protobuf | Ready-made tools for sending structured messages between programs. He wants you to know the trade-offs vs simpler options |
| **Distributed systems** | Several computers working together (server A sending to server B) |
| Pre-allocation, ring buffers | Speed tricks: setting up memory ahead of time instead of while the program runs |
| Percentiles, histograms | Measuring speed properly, e.g. "99% of orders took under X microseconds" |
| Worst-case thinking | How your program behaves when the amount of data gets huge |
| **Profiling and benchmarking** (Linux `perf`, flame graphs) | Measuring where your program spends its time, and proving it got faster |
| **Unit vs integration tests** | Testing small pieces on their own vs testing whole parts working together (like a client talking to a server) |
| **README** | The front page of your project. An interviewer should understand what it is and how to run it in 5 to 10 minutes |

## 3 pitfalls

1. **Tutorial hell.** Watching videos feels productive, but you need to stop and **solve problems** to check you really understand.
2. **Starting a new project before finishing the last one.** Usually because the plan was too big. Build the skills first, and the impressive part follows.
3. **Letting AI build your project.** If it's on your résumé, every part of it can be questioned in an interview, so you need to understand **100%** of it.

## His summary steps

1. Learn the topics.
2. Decide what to build around them.
3. Check it's at least a bit impressive: ask someone in the industry, or ask online.
4. Work out which skills you're missing, then commit fully.
5. **Stop delaying**, and **plan**: write down what you'll do each day (a to-do board or a journal) so you hold yourself accountable.

## How this fits me right now

- **Useful now:** the 4 questions, the 3 pitfalls (especially pitfall 3, which is why I ask for hints first), and finishing every project before starting the next. 100 Days does that one day at a time.
- **Not for now:** the C++, networking and Linux list is for **quant developer** jobs specifically. It's far beyond Day 22 of Python. Only worth coming back to if I decide I want that career.
- **Paid coaching:** not needed to learn the basics. Free resources (this course, CS50, the LeetCode list in `TODO.md`) cover the fundamentals.
