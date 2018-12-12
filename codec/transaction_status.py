from enum import Enum


class TransactionStatus(Enum):
    TRANSACTION_STATUS_COMMITTED = 'COMMITTED'
    TRANSACTION_STATUS_DUPLICATE_TRANSACTION_ALREADY_COMMITTED = 'DUPLICATE_TRANSACTION_ALREADY_COMMITTED'
    TRANSACTION_STATUS_PENDING = 'PENDING'
    TRANSACTION_STATUS_DUPLICATE_TRANSACTION_ALREADY_PENDING = 'DUPLICATE_TRANSACTION_ALREADY_PENDING'
    TRANSACTION_STATUS_NO_RECORD_FOUND = 'NO_RECORD_FOUND'
    TRANSACTION_STATUS_REJECTED_UNSUPPORTED_VERSION = 'REJECTED_UNSUPPORTED_VERSION'
    TRANSACTION_STATUS_REJECTED_VIRTUAL_CHAIN_MISMATCH = 'REJECTED_VIRTUAL_CHAIN_MISMATCH'
    TRANSACTION_STATUS_REJECTED_TIMESTAMP_WINDOW_EXCEEDED = 'REJECTED_TIMESTAMP_WINDOW_EXCEEDED'
    TRANSACTION_STATUS_REJECTED_SIGNATURE_MISMATCH = 'REJECTED_SIGNATURE_MISMATCH'
    TRANSACTION_STATUS_REJECTED_UNKNOWN_SIGNER_SCHEME = 'REJECTED_UNKNOWN_SIGNER_SCHEME'
    TRANSACTION_STATUS_REJECTED_GLOBAL_PRE_ORDER = 'REJECTED_GLOBAL_PRE_ORDER'
    TRANSACTION_STATUS_REJECTED_VIRTUAL_CHAIN_PRE_ORDER = 'REJECTED_VIRTUAL_CHAIN_PRE_ORDER'
    TRANSACTION_STATUS_REJECTED_SMART_CONTRACT_PRE_ORDER = 'REJECTED_SMART_CONTRACT_PRE_ORDER'
    TRANSACTION_STATUS_REJECTED_TIMESTAMP_AHEAD_OF_NODE_TIME = 'REJECTED_TIMESTAMP_AHEAD_OF_NODE_TIME'
    TRANSACTION_STATUS_REJECTED_CONGESTION = 'REJECTED_CONGESTION'


def transaction_status_decode(transaction_status: int) -> TransactionStatus:
    if transaction_status == 0:
        raise ValueError('reserved TransactionStatus received')
    elif transaction_status == 1:
        return TransactionStatus.TRANSACTION_STATUS_COMMITTED
    elif transaction_status == 2:
        return TransactionStatus.TRANSACTION_STATUS_DUPLICATE_TRANSACTION_ALREADY_COMMITTED
    elif transaction_status == 3:
        return TransactionStatus.TRANSACTION_STATUS_PENDING
    elif transaction_status == 4:
        return TransactionStatus.TRANSACTION_STATUS_DUPLICATE_TRANSACTION_ALREADY_PENDING
    elif transaction_status == 6:
        return TransactionStatus.TRANSACTION_STATUS_NO_RECORD_FOUND
    elif transaction_status == 7:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_UNSUPPORTED_VERSION
    elif transaction_status == 8:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_VIRTUAL_CHAIN_MISMATCH
    elif transaction_status == 9:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_TIMESTAMP_WINDOW_EXCEEDED
    elif transaction_status == 10:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_SIGNATURE_MISMATCH
    elif transaction_status == 11:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_UNKNOWN_SIGNER_SCHEME
    elif transaction_status == 12:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_GLOBAL_PRE_ORDER
    elif transaction_status == 13:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_VIRTUAL_CHAIN_PRE_ORDER
    elif transaction_status == 14:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_SMART_CONTRACT_PRE_ORDER
    elif transaction_status == 15:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_TIMESTAMP_AHEAD_OF_NODE_TIME
    elif transaction_status == 16:
        return TransactionStatus.TRANSACTION_STATUS_REJECTED_CONGESTION
    else:
        raise ValueError(f'unsupported TransactionStatus received: {transaction_status}')
