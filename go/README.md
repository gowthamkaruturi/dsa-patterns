# Algorithm Patterns & System Design Practice

Personal DSA and System Design interview prep repo. Used alongside the AI Engineer roadmap for well-rounded interview readiness.

## DSA Patterns
- [ ] Sliding Window
- [ ] Two Pointers
- [ ] Fast & Slow Pointers
- [ ] Merge Intervals
- [ ] Cyclic Sort
- [ ] In-place Reversal of a Linked List
- [ ] Tree Breadth-First Search
- [ ] Tree Depth-First Search
- [ ] Two Heaps
- [ ] Subsets
- [ ] Modified Binary Search
- [ ] Top K Elements
- [ ] K-way Merge
- [ ] Topological Sort
- [ ] Backtracking
- [ ] Dynamic Programming (0/1 Knapsack, Unbounded Knapsack, Fibonacci, Palindromic Subsequence)
- [ ] Greedy Algorithms
- [ ] Trie
- [ ] Union Find / Disjoint Set
- [ ] Bitwise Manipulation
- Resource: NeetCode.io (see neetcode-submissions repo), existing slidingwindow/ and utils/ folders here

## System Design Fundamentals
- [ ] Scalability: vertical vs horizontal
- [ ] Availability & reliability
- [ ] Consistency models & CAP theorem
- [ ] Load balancing strategies
- [ ] Caching strategies and invalidation
- [ ] Database indexing, sharding, replication
- [ ] Message queues & pub/sub
- [ ] CDN basics
- [ ] Rate limiting algorithms
- [ ] API design: REST vs gRPC vs GraphQL
- Resource: "System Design Interview" by Alex Xu, ByteByteGo YouTube, Gaurav Sen YouTube

## NoSQL Database Design Notes (consolidated from dynamodb repo)
Amazon DynamoDB is a managed, serverless NoSQL database built for consistent performance at scale. Key principles to know for system design interviews:

- Serverless architecture - no server provisioning or management required.
- Automatic partitioning and scaling to handle high, variable request rates.
- Data is replicated across multiple AWS Availability Zones for durability and high availability.
- DynamoDB Streams enable event-driven patterns via Lambda triggers.
- Supports both key-value and flexible document data models.
- ACID transactions are supported for data integrity.
- Security via VPC isolation, encryption at rest/in transit, and IAM access control.

Single-table vs multi-table design:
- Single-table design works best with well-known access patterns, and can be more cost-efficient and faster for retrieval, at the cost of implementation complexity.
- Multi-table design is more intuitive coming from relational databases, offers better isolation and independent scaling per table, but can mean higher cost and extra requests for related data.

Capacity modes:
- On-demand: DynamoDB scales automatically to actual traffic; good for unpredictable workloads, pay-per-request.
- Provisioned: you specify expected read/write throughput (optionally with auto-scaling); more cost-effective for predictable, steady workloads.

Scaling implications tie back to the single vs multi-table decision: single-table centralizes and simplifies scaling/cost management, while multi-table allows independent, granular scaling and better workload isolation per table.

- [ ] Review DynamoDB single-table vs multi-table tradeoffs
- [ ] Review on-demand vs provisioned capacity tradeoffs
- [ ] Practice: design a system using DynamoDB as the primary data store

## System Design Practice Problems
- [ ] Design a URL Shortener
- [ ] Design a Rate Limiter
- [ ] Design a Distributed Cache
- [ ] Design a Chat Application
- [ ] Design a Notification System
- [ ] Design a News Feed / Timeline
- [ ] Design a Ride-Sharing App
- [ ] Design a Distributed File Storage System

## Existing Folders
- slidingwindow/ - sliding window pattern solutions
- utils/ - helper utilities

## Notes
Check boxes off as each pattern/topic is completed. Add new solutions under a folder per topic, e.g. system-design/url-shortener/notes.md.
