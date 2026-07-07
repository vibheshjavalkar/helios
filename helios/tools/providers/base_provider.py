from abc import ABC, abstractmethod

class ContextProvider(ABC):
    @abstractmethod
    def get_context(self, task: str, mode: str = "SAFE") -> dict:
        """
        Retrieves the execution context for a given task.

        Parameters
        ----------
        task : str
            The name or description of the task.
        mode : str, optional
            The execution mode ("SAFE" or "DEMO").

        Returns
        -------
        dict
            A structured context dictionary.
        """
        pass
