from client_sdk_python.packages.eth_utils import (
    is_string,
)

from client_sdk_python.utils.formatters import (
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatters_to_dict,
)

from .formatting import (
    construct_formatting_middleware,
)

FILTER_PARAM_NORMALIZERS = apply_formatters_to_dict({
    'address': apply_formatter_if(is_string, lambda x: [x])})

METHOD_NORMALIZERS = {
    'platon_getLogs': apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0),
    'platon_newFilter': apply_formatter_at_index(FILTER_PARAM_NORMALIZERS, 0)
}

request_parameter_normalizer = construct_formatting_middleware(
    request_formatters=METHOD_NORMALIZERS,
)
