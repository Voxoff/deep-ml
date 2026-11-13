import numpy as np
from functools import reduce

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    OPS = {
        'square': (lambda u: u**2, lambda u: 2 * u),
        'sin':    (np.sin,         np.cos),
        'exp':    (np.exp,         np.exp),
        'log':    (np.log,         lambda u: 1 / u),
    }
    _, total_df = reduce(
        lambda outer, inner: (
            lambda u: outer[0](inner[0](u)),
            lambda u: outer[1](inner[0](u)) * inner[1](u),
        ),
        (OPS[name] for name in functions),
    )

    return float(total_df(x))
    # gx = OPS[functions[1]][0](x)
    
    # return OPS[functions[0]][1](gx)* (OPS[functions[1]][1](x))

