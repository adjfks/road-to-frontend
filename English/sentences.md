# 句子

1. *multiple*  window event loops *could be cooperatively scheduled in a single thread.*

   *多个*窗口事件循环，可以在单个线程中协同调度

2. Some elements have tasks that trigger in response to DOM manipulation

    有些元素具有响应DOM操作而触发的任务

3. A series of steps specifying the work to be done by the task.

   指定任务要完成的工作的一系列步骤。

4. *Essentially,* task sources *are used within standards to separate logically-different types of tasks, which a user agent might wish to distinguish between.* [Task queues](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) *are used by user agents to coalesce task sources within a given* [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop)*.*

   *本质上，*任务源*在标准中用于分离逻辑上不同类型的任务，用户代理可能希望区分这些任务。任务队列*由用户代理用于在给定的*[事件循环]内合并任务源

5. Each event loop has a currently running task, which is either a task or null. Initially, this is null. It is used to handle reentrancy.

   每个[事件循环有一个当前正在运行的任务，该任务可以是task或空。最初，这是空的。它用于处理重入。





