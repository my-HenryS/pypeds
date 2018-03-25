from pypeds.entity import Agent, Goal ,RotateAgent
from pypeds.scene import SceneListener
from abc import ABC, abstractmethod


class Strategy(SceneListener):
    """ A strategy set each agents' path in a scene.

    """

    def __init__(self):
        super().__init__()

    @property
    def agents(self):
        return self.scene.entities_of_type(Agent)

    @property
    def rotateagent(self):
        return self.scene.entities_of_type(RotateAgent)

    @property
    def goals(self):
        return self.scene.entities_of_type(Goal)

    def on_added(self):
        pass

    @abstractmethod
    def on_begin(self):
        """ Strategy will set path for each agent towards goal

        """
        pass

    @abstractmethod
    def on_stepped(self):
        """ Dynamic strategy will set agent's path within certain interval

        """
        pass

    def on_removed(self):
        pass


class StaticStrategy(Strategy):
    def on_stepped(self):
        """ Static strategy will not modify agent's path after scene starts

        """
        pass


class Path(ABC):
    @abstractmethod
    def next_step(self, pos):
        pass
