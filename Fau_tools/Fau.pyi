import torch
from torch import nn
import torch.utils.data as tdata

def calc_time(function) -> None: ...

def show_progress(now: int, total: int, loss: float=None, accuracy: float=None) -> None: ...

def calc_accuracy(model: nn.Module, test_loader: tdata.DataLoader, DEVICE: torch.device=None) -> float: ...
