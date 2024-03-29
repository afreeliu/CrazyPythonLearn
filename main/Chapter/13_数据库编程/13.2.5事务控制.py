

'''

    事务控制

    事务是由一步或几步数据库操作序列组成的逻辑执行单元，这一系列操作要么全部执行，要么全部放弃执行。程序和事务是两个不同的概念。
    一般而言，在一段程序中可能包含多个事务。

    事务具备 4 中特性：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）和持续性（Durability）。这 4 中特性
    也简称为 ACID。

    原子性： 事务是应用中最小的执行单位，就如原子是自然界的最小颗粒，具有不可再分的特征一样，事务是应用中不可再分的最小逻辑执行体

    一致性： 事务执行的结果，必须使数据库从一种一致性状态变到另一种一致性状态。当数据库只包含事务成功提交的结果时，数据库处于一致性状态。
            如果系统运行发生中断，某个事务尚未完成而被迫中断，而该未完成的事务对数据库所做的修改已被写入数据库中，此时数据库就处于一种
            不正确的状态。比如银行在两个账户之间转账，从 A 账号向 B 账户转入 1000 元，系统先减少 A 账户的 1000 元，然后再为 B 账户
            增加 1000 元。如果全部执行成功，数据库处于一致性状态；如果仅执行完 A 账户金额的修改，而没有增加 B 账户的金额，则数据库就
            处于补一种状态。因此，一致性是通过原子性来保证的。

    隔离性： 各个事务的执行互不干扰，任意一个事务的内部操作对其他并发的事务都是隔离的。也就是说，并发执行的事务之间不能看到对方的中间状态
            ，它们不能互相影响。

    持续性： 持续性也称为持久性（Persistence），指事物一旦提交，对数据所做的任何改变都要记录到永久存储中，通常就是保存到物理数据库中

    当事务所包含的任意一个数据库操作执行失败后，应该回滚（rollback）事务，使在该事务中所做的修改全部失效。事务回滚有两种方式：
    显式回滚和自动回滚。

    显式回滚： 调用数据库连接对象的回滚

    自动回滚： 系统错误，或者强行退出。


'''


