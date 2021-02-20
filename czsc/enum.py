# coding: utf-8

from enum import Enum

class Mark(Enum):
    D = "底分型"
    G = "顶分型"

class Direction(Enum):
    Up = "向上"
    Down = "向下"

class Freq(Enum):
    F1 = "1分钟"
    F5 = "5分钟"
    F15 = "15分钟"
    F30 = "30分钟"
    F60 = "60分钟"
    D = "日线"
    W = "周线"
    M = "月线"

class Signals(Enum):
    Other = "其他"

    # 信号值编码规则：
    # 笔数：X3 - 三笔信号；X5 - 五笔信号；X7 - 七笔信号；X9 - 九笔信号；
    # 多空：L - 多头信号；S - 空头信号；
    # 编号：A0 - A类基础型；A1 - A类变种1 ... 以此类推
    # 组合规则：笔数_多空_编号；如 X5LA0 表示五笔多头信号A0
    # ============================================================================================

    # 三笔形态信号
    X3LA0 = "X3LA0~向下不重合"
    X3LB0 = "X3LB0~向下奔走型中枢"
    X3LC0 = "X3LC0~向下三角收敛中枢"
    X3LD0 = "X3LD0~向下三角扩张中枢"
    X3LE0 = "X3LE0~向下盘背中枢"
    X3LF0 = "X3LF0~向下无背中枢"

    X3SA0 = "X3SA0~向上不重合"
    X3SB0 = "X3SB0~向上奔走型中枢"
    X3SC0 = "X3SC0~向上三角收敛中枢"
    X3SD0 = "X3SD0~向上三角扩张中枢"
    X3SE0 = "X3SE0~向上盘背中枢"
    X3SF0 = "X3SF0~向上无背中枢"

    # 五笔形态信号
    # 具体描述：https://blog.csdn.net/baidu_25764509/article/details/113639353
    X5LA0 = "X5LA0~aAb式底背弛"
    X5LB0 = "X5LB0~三买"
    X5LC0 = "X5LC0~类趋势底背驰"
    X5LD0 = "X5LD0~向下三角扩张中枢"
    X5LE0 = "X5LE0~向下三角收敛中枢"
    X5LF0 = "X5LF0~大级别底分"

    X5SA0 = "X5SA0~aAb式顶背驰"
    X5SB0 = "X5SB0~三卖"
    X5SC0 = "X5SC0~类趋势顶背驰"
    X5SD0 = "X5SD0~向上三角扩张中枢"
    X5SE0 = "X5SE0~向上三角收敛中枢"
    X5SF0 = "X5SF0~大级别顶分"

    # 七笔多头信号
    # 具体描述：https://blog.csdn.net/baidu_25764509/article/details/113649988
    X7LA0 = "X7LA0~aAbcd式底背弛"
    X7LB0 = "X7LB0~abcAd式底背弛"
    X7LC0 = "X7LC0~aAb式底背弛"
    X7LD0 = "X7LD0~类趋势底背弛"
    X7LE0 = "X7LE0~BaA式右侧底"
    X7LF0 = "X7LF0~类趋势底背弛强反弹后不创新低"

    X7SA0 = "X7SA0~aAbcd式顶背驰"
    X7SB0 = "X7SB0~abcAd式顶背驰"
    X7SC0 = "X7SC0~aAb式顶背驰"
    X7SD0 = "X7SD0~类趋势顶背驰"
    X7SE0 = "X7SE0~BaA式右侧顶"
    X7SF0 = "X7SF0~类趋势顶背驰强反弹后不创新高"

    # 九笔多头信号
    X9LA0 = "X9LA0~aAbBc式向下趋势底背弛"
    X9LB0 = "X9LB0~aAb式底背弛"
    X9LC0 = "X9LC0~aAbcd式底背弛"

    X9SA0 = "X9SA0~aAbBc式向上趋势顶背驰"
    X9SB0 = "X9SB0~aAb式顶背弛"
    X9SC0 = "X9SC0~aAbcd式顶背弛"

class Factors(Enum):
    Other = "其他"
    # 因子值编码规则：
    # 级别：C1 - 1分钟；C2 - 5分钟; C3 - 15分钟; C4 - 30分钟; C5 - 60分钟; C6 - 日线;
    # 类型：
    #   L1 - 向下笔转折右侧；L2 - 向下笔转折左侧；L3 - 向上笔中继右侧；L4 - 向上笔中继左侧；
    #   S1 - 向上笔转折右侧；S2 - 向上笔转折左侧；S3 - 向下笔中继右侧；S4 - 向下笔中继左侧；
    # 编号：A0 - A类基础型；A1 - A类变种1 ... 以此类推
    # 组合规则为 本级别_次级别_类型_编号
    # ============================================================================================
    C6C5L1A0 = "C6C5L1A0~60分钟三买"
    C6C5L1A1 = "C6C5L1A1~60分钟三买&60分钟最近一个向上笔创新高"
    C6C5L1A2 = "C6C5L1A2~60分钟三买&大级别倒2顶背驰"
    C6C5L1A3 = "C6C5L1A3~60分钟三买&大级别倒1底背驰"

    C6C4L1A0 = "C6C4L1A0~30分钟三买"
    C6C4L1A1 = "C6C4L1A1~30分钟三买&30分钟最近一个向上笔创新高"
    C6C4L1A2 = "C6C4L1A2~30分钟三买&大级别倒2顶背驰"
    C6C4L1A3 = "C6C4L1A3~30分钟三买&大级别倒1底背驰"

    C6C3L1A0 = "C6C3L1A0~15分钟三买"
    C6C3L1A1 = "C6C3L1A1~15分钟三买&15分钟最近一个向上笔创新高"
    C6C3L1A2 = "C6C3L1A2~15分钟三买&大级别倒2顶背驰"
    C6C3L1A3 = "C6C3L1A3~15分钟三买&大级别倒1底背驰"

    C5C3L1A0 = "C5C3L1A0~15分钟三买"
    C5C3L1A1 = "C5C3L1A1~15分钟三买&15分钟最近一个向上笔创新高"
    C5C3L1A2 = "C5C3L1A2~15分钟三买&大级别倒2顶背驰"
    C5C3L1A3 = "C5C3L1A3~15分钟三买&大级别倒1底背驰"

    C5C2L1A0 = "C5C2L1A0~5分钟三买"
    C5C2L1A1 = "C5C2L1A1~5分钟三买&5分钟最近一个向上笔创新高"
    C5C2L1A2 = "C5C2L1A2~5分钟三买&大级别倒2顶背驰"
    C5C2L1A3 = "C5C2L1A3~5分钟三买&大级别倒1底背驰"

    # --------------------------------------------------------------------------------------------
    C6C5L1B0 = "C6C5L1B0~日线第N笔超强底分&15分钟近七笔为BaA式右侧底"
    C6C4L1B0 = "C6C4L1B0~日线第N笔超强底分&5分钟近七笔为BaA式右侧底"
    C6C3L1B0 = "C6C3L1B0~日线第N笔超强底分&1分钟近七笔为BaA式右侧底"

    C5C3L1B0 = "C5C3L1B0~60分钟第N笔超强底分&1分钟近七笔为BaA式右侧底"
    C5C2L1B0 = "C5C2L1B0~60分钟第N笔超强底分&1分钟近七笔为BaA式右侧底"
    # --------------------------------------------------------------------------------------------
    C6C5L2A0 = "C6C5L2A0~60分钟近五笔为底背弛"
    C6C4L2A0 = "C6C4L2A0~30分钟近五笔为底背弛"
    C6C3L2A0 = "C6C3L2A0~15分钟近五笔为底背弛"

    C5C3L2A0 = "C5C3L2A0~15分钟近五笔为底背弛"
    C5C2L2A0 = "C5C2L2A0~5分钟近五笔为底背弛"
    # --------------------------------------------------------------------------------------------
    C6C5L2B0 = "C6C5L2B0~60分钟近七笔为底背弛"
    C6C4L2B0 = "C6C4L2B0~30分钟近七笔为底背弛"
    C6C3L2B0 = "C6C3L2B0~15分钟近七笔为底背弛"

    C5C3L2B0 = "C5C3L2B0~15分钟近七笔为底背弛"
    C5C2L2B0 = "C5C2L2B0~5分钟近七笔为底背弛"
    # --------------------------------------------------------------------------------------------
    C6C5L2C0 = "C6C5L2C0~60分钟近九笔为底背弛"
    C6C5L2C1 = "C6C5L2C1~60分钟近九笔为aAbBc式底背弛"

    C6C4L2C0 = "C6C4L2C0~30分钟近九笔为底背弛"
    C6C4L2C1 = "C6C4L2C1~30分钟近九笔为aAbBc式底背弛"

    C6C3L2C0 = "C6C3L2C0~15分钟近九笔为底背弛"
    C6C3L2C1 = "C6C3L2C1~15分钟近九笔为aAbBc式底背弛"

    C5C3L2C0 = "C5C3L2C0~15分钟近九笔为底背弛"
    C5C3L2C1 = "C5C3L2C1~15分钟近九笔为aAbBc式底背弛"

    C5C2L2C0 = "C5C2L2C0~5分钟近九笔为底背弛"
    C5C2L2C1 = "C5C2L2C1~5分钟近九笔为aAbBc式底背弛"
    # --------------------------------------------------------------------------------------------
    C6C5L3A0 = "C6C5L3A0~60分钟近七笔为BaA式右侧底"
    C6C4L3A0 = "C6C4L3A0~30分钟近七笔为BaA式右侧底"
    C6C3L3A0 = "C6C3L3A0~15分钟近七笔为BaA式右侧底"

    C5C3L3A0 = "C5C3L3A0~1分钟近七笔为BaA式右侧底"
    C5C2L3A0 = "C5C2L3A0~1分钟近七笔为BaA式右侧底"
    # --------------------------------------------------------------------------------------------
    C6C5L4A0 = "C6C5L4A0~15分钟近七笔为底背弛"
    C6C4L4A0 = "C6C4L4A0~5分钟近七笔为底背弛"
    C6C3L4A0 = "C6C3L4A0~1分钟近七笔为底背弛"

    C5C3L4A0 = "C5C3L4A0~1分钟近七笔为底背弛"
    C5C2L4A0 = "C5C2L4A0~1分钟近七笔为底背弛"
    # --------------------------------------------------------------------------------------------
    C6C5S1A0 = "C6C5S1A0~60分钟三卖"
    C6C5S1A1 = "C6C5S1A1~60分钟三卖&60分钟最近一个向下笔创新低"
    C6C5S1A2 = "C6C5S1A2~60分钟三卖&大级别倒2底背驰"
    C6C5S1A3 = "C6C5S1A3~60分钟三卖&大级别倒1顶背驰"

    C6C4S1A0 = "C6C4S1A0~30分钟三卖"
    C6C4S1A1 = "C6C4S1A1~30分钟三卖&30分钟最近一个向下笔创新低"
    C6C4S1A2 = "C6C4S1A2~30分钟三卖&大级别倒2底背驰"
    C6C4S1A3 = "C6C4S1A3~30分钟三卖&大级别倒1顶背驰"

    C6C3S1A0 = "C6C3S1A0~15分钟三卖"
    C6C3S1A1 = "C6C3S1A1~15分钟三卖&15分钟最近一个向下笔创新低"
    C6C3S1A2 = "C6C3S1A2~15分钟三卖&大级别倒2底背驰"
    C6C3S1A3 = "C6C3S1A3~15分钟三卖&大级别倒1顶背驰"

    C5C3S1A0 = "C5C3S1A0~15分钟三卖"
    C5C3S1A1 = "C5C3S1A1~15分钟三卖&15分钟最近一个向下笔创新低"
    C5C3S1A2 = "C5C3S1A2~15分钟三卖&大级别倒2底背驰"
    C5C3S1A3 = "C5C3S1A3~15分钟三卖&大级别倒1顶背驰"

    C5C2S1A0 = "C5C2S1A0~5分钟三卖"
    C5C2S1A1 = "C5C2S1A1~5分钟三卖&5分钟最近一个向下笔创新低"
    C5C2S1A2 = "C5C2S1A2~5分钟三卖&大级别倒2底背驰"
    C5C2S1A3 = "C5C2S1A3~5分钟三卖&大级别倒1顶背驰"
    # --------------------------------------------------------------------------------------------
    C6C5S1B0 = "C6C5S1B0~60分钟近五笔为aAb式顶背驰"
    C6C4S1B0 = "C6C4S1B0~30分钟近五笔为aAb式顶背驰"
    C6C3S1B0 = "C6C3S1B0~15分钟近五笔为aAb式顶背驰"

    C5C3S1B0 = "C5C3S1B0~15分钟近五笔为aAb式顶背驰"
    C5C2S1B0 = "C5C2S1B0~5分钟近五笔为aAb式顶背驰"
    # --------------------------------------------------------------------------------------------
    C6C5S2A0 = "C6C5S2A0~60分钟近七笔为顶背弛"
    C6C4S2A0 = "C6C4S2A0~30分钟近七笔为顶背弛"
    C6C3S2A0 = "C6C3S2A0~15分钟近七笔为顶背弛"
    C5C3S2A0 = "C5C3S2A0~15分钟近七笔为顶背弛"
    C5C2S2A0 = "C5C2S2A0~5分钟近七笔为顶背弛"
    # --------------------------------------------------------------------------------------------
    C6C5S3A0 = "C6C5S3A0~60分钟近五笔为大级别顶分"
    C6C4S3A0 = "C6C4S3A0~30分钟近五笔为大级别顶分"
    C6C3S3A0 = "C6C3S3A0~15分钟近五笔为大级别顶分"

    C5C3S3A0 = "C5C3S3A0~15分钟近五笔为大级别顶分"
    C5C2S3A0 = "C5C2S3A0~5分钟近五笔为大级别顶分"
    # --------------------------------------------------------------------------------------------
    C6C5S4A0 = "C6C5S4A0~15分钟近五笔为aAb式顶背驰"
    C6C4S4A0 = "C6C4S4A0~5分钟近五笔为aAb式顶背驰"
    C6C3S4A0 = "C6C3S4A0~1分钟近五笔为aAb式顶背驰"

    C5C3S4A0 = "C5C3S4A0~1分钟近五笔为aAb式顶背驰"
    C5C2S4A0 = "C5C2S4A0~1分钟近五笔为aAb式顶背驰"
    # --------------------------------------------------------------------------------------------

