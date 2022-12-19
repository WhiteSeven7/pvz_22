from copy import copy

from .fpn import FPN3


class AbstractTiming:
    def __init__(self, master, value=FPN3(0, 0), pause_status=False, speed=FPN3(1)):
        """
        抽象时钟
        :param master: 主人
        :param value: 指定初值，其拷贝会被赋值给self.value，无需担心重复
        :param pause_status: 暂停状态
        :param speed: 速度
        """
        self.master = master
        self.__value = copy(value)
        self.__pause_status = pause_status
        self.speed = copy(speed)

    def tick(self, speed):
        if self.pause:
            return
        self.__value += self.speed * speed

    def realvalue(self):
        """
        返回内部value的拷贝，不会影响内部value的值
        :return: 内部value的拷贝
        """
        return copy(self.__value)

    def value(self):
        return int(self.__value)

    # 用pause，unpause，changepause改变pause状态
    def pause(self):
        self.__pause_status = True

    def unpause(self):
        self.__pause_status = False

    def changepause(self):
        self.__pause_status = not self.__pause_status


class InfiniteTiming(AbstractTiming):
    ...


class FiniteTiming(AbstractTiming):
    def __init__(self, master, maxvalue, value=FPN3(0, 0), pause_status=False, speed=FPN3(1)):
        super().__init__(master, value, pause_status, speed)
        self.maxvalue = copy(maxvalue)
        self.user_end = self.__class__.user_end

    def tick(self, speed):
        if self.__pause_status:
            return
        self.__value = self.speed * speed
        if self.__value >= self.maxvalue:
            self.user_end()
            self.pause()

    @classmethod
    def user_end(cls):
        """由外部设置的终止命令"""
        return


class LoopTiming(FiniteTiming):
    def tick(self, speed):
        if self.__pause_status:
            return
        self.__value = self.speed * speed
        if self.__value >= self.maxvalue:
            self.user_end()
            self.__value = FPN3()
            self.user_end = self.__class__.user_end


IT = ITiming = InfiniteTiming
FT = FTiming = FiniteTiming
LT = LTiming = LoopTiming
