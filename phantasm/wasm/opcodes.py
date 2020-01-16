"""Defines mappings of opcodes to their info structures."""
from enum import Enum, IntEnum
from .immtypes import *


class InsFlag(IntEnum):
    ENTER_BLOCK = 1 << 0
    LEAVE_BLOCK = 1 << 1
    BRANCH = 1 << 2
    NO_FLOW = 1 << 3


class Opcode(Enum):
    UNREACHABLE = 0x00, 'unreachable', None, InsFlag.NO_FLOW
    NOP = 0x01, 'nop', None, 0
    BLOCK = 0x02, 'block', BlockImm(), InsFlag.ENTER_BLOCK
    LOOP = 0x03, 'loop', BlockImm(), InsFlag.ENTER_BLOCK
    IF = 0x04, 'if', BlockImm(), InsFlag.ENTER_BLOCK
    ELSE = 0x05, 'else', None, InsFlag.ENTER_BLOCK | InsFlag.LEAVE_BLOCK
    END = 0x0b, 'end', None, InsFlag.LEAVE_BLOCK
    BR = 0x0c, 'br', BranchImm(), InsFlag.BRANCH
    BR_IF = 0x0d, 'br_if', BranchImm(), InsFlag.BRANCH
    BR_TABLE = 0x0e, 'br_table', BranchTableImm(), InsFlag.BRANCH
    RETURN = 0x0f, 'return', None, InsFlag.NO_FLOW

    CALL = 0x10, 'call', CallImm(), InsFlag.BRANCH
    CALL_INDIRECT = 0x11, 'call_indirect', CallIndirectImm(), InsFlag.BRANCH

    DROP = 0x1a, 'drop', None, 0
    SELECT = 0x1b, 'select', None, 0

    GET_LOCAL = 0x20, 'get_local', LocalVarXsImm(), 0
    SET_LOCAL = 0x21, 'set_local', LocalVarXsImm(), 0
    TEE_LOCAL = 0x22, 'tee_local', LocalVarXsImm(), 0
    GET_GLOBAL = 0x23, 'get_global', GlobalVarXsImm(), 0
    SET_GLOBAL = 0x24, 'set_global', GlobalVarXsImm(), 0

    I32_LOAD = 0x28, 'i32.load', MemoryImm(), 0
    I64_LOAD = 0x29, 'i64.load', MemoryImm(), 0
    F32_LOAD = 0x2a, 'f32.load', MemoryImm(), 0
    F64_LOAD = 0x2b, 'f64.load', MemoryImm(), 0
    I32_LOAD8_S = 0x2c, 'i32.load8_s', MemoryImm(), 0
    I32_LOAD8_U = 0x2d, 'i32.load8_u', MemoryImm(), 0
    I32_LOAD16_S = 0x2e, 'i32.load16_s', MemoryImm(), 0
    I32_LOAD16_U = 0x2f, 'i32.load16_u', MemoryImm(), 0
    I64_LOAD8_S = 0x30, 'i64.load8_s', MemoryImm(), 0
    I64_LOAD8_U = 0x31, 'i64.load8_u', MemoryImm(), 0
    I64_LOAD16_S = 0x32, 'i64.load16_s', MemoryImm(), 0
    I64_LOAD16_U = 0x33, 'i64.load16_u', MemoryImm(), 0
    I64_LOAD32_S = 0x34, 'i64.load32_s', MemoryImm(), 0
    I64_LOAD32_U = 0x35, 'i64.load32_u', MemoryImm(), 0
    I32_STORE = 0x36, 'i32.store', MemoryImm(), 0
    I64_STORE = 0x37, 'i64.store', MemoryImm(), 0
    F32_STORE = 0x38, 'f32.store', MemoryImm(), 0
    F64_STORE = 0x39, 'f64.store', MemoryImm(), 0
    I32_STORE8 = 0x3a, 'i32.store8', MemoryImm(), 0
    I32_STORE16 = 0x3b, 'i32.store16', MemoryImm(), 0
    I64_STORE8 = 0x3c, 'i64.store8', MemoryImm(), 0
    I64_STORE16 = 0x3d, 'i64.store16', MemoryImm(), 0
    I64_STORE32 = 0x3e, 'i64.store32', MemoryImm(), 0
    CURRENT_MEMORY = 0x3f, 'current_memory', CurGrowMemImm(), 0
    GROW_MEMORY = 0x40, 'grow_memory', CurGrowMemImm(), 0

    I32_CONST = 0x41, 'i32.const', I32ConstImm(), 0
    I64_CONST = 0x42, 'i64.const', I64ConstImm(), 0
    F32_CONST = 0x43, 'f32.const', F32ConstImm(), 0
    F64_CONST = 0x44, 'f64.const', F64ConstImm(), 0

    I32_EQZ = 0x45, 'i32.eqz', None, 0
    I32_EQ = 0x46, 'i32.eq', None, 0
    I32_NE = 0x47, 'i32.ne', None, 0
    I32_LT_S = 0x48, 'i32.lt_s', None, 0
    I32_LT_U = 0x49, 'i32.lt_u', None, 0
    I32_GT_S = 0x4a, 'i32.gt_s', None, 0
    I32_GT_U = 0x4b, 'i32.gt_u', None, 0
    I32_LE_S = 0x4c, 'i32.le_s', None, 0
    I32_LE_U = 0x4d, 'i32.le_u', None, 0
    I32_GE_S = 0x4e, 'i32.ge_s', None, 0
    I32_GE_U = 0x4f, 'i32.ge_u', None, 0
    I64_EQZ = 0x50, 'i64.eqz', None, 0
    I64_EQ = 0x51, 'i64.eq', None, 0
    I64_NE = 0x52, 'i64.ne', None, 0
    I64_LT_S = 0x53, 'i64.lt_s', None, 0
    I64_LT_U = 0x54, 'i64.lt_u', None, 0
    I64_GT_S = 0x55, 'i64.gt_s', None, 0
    I64_GT_U = 0x56, 'i64.gt_u', None, 0
    I64_LE_S = 0x57, 'i64.le_s', None, 0
    I64_LE_U = 0x58, 'i64.le_u', None, 0
    I64_GE_S = 0x59, 'i64.ge_s', None, 0
    I64_GE_U = 0x5a, 'i64.ge_u', None, 0
    F32_EQ = 0x5b, 'f32.eq', None, 0
    F32_NE = 0x5c, 'f32.ne', None, 0
    F32_LT = 0x5d, 'f32.lt', None, 0
    F32_GT = 0x5e, 'f32.gt', None, 0
    F32_LE = 0x5f, 'f32.le', None, 0
    F32_GE = 0x60, 'f32.ge', None, 0
    F64_EQ = 0x61, 'f64.eq', None, 0
    F64_NE = 0x62, 'f64.ne', None, 0
    F64_LT = 0x63, 'f64.lt', None, 0
    F64_GT = 0x64, 'f64.gt', None, 0
    F64_LE = 0x65, 'f64.le', None, 0
    F64_GE = 0x66, 'f64.ge', None, 0

    I32_CLZ = 0x67, 'i32.clz', None, 0
    I32_CTZ = 0x68, 'i32.ctz', None, 0
    I32_POPCNT = 0x69, 'i32.popcnt', None, 0
    I32_ADD = 0x6a, 'i32.add', None, 0
    I32_SUB = 0x6b, 'i32.sub', None, 0
    I32_MUL = 0x6c, 'i32.mul', None, 0
    I32_DIV_S = 0x6d, 'i32.div_s', None, 0
    I32_DIV_U = 0x6e, 'i32.div_u', None, 0
    I32_REM_S = 0x6f, 'i32.rem_s', None, 0
    I32_REM_U = 0x70, 'i32.rem_u', None, 0
    I32_AND = 0x71, 'i32.and', None, 0
    I32_OR = 0x72, 'i32.or', None, 0
    I32_XOR = 0x73, 'i32.xor', None, 0
    I32_SHL = 0x74, 'i32.shl', None, 0
    I32_SHR_S = 0x75, 'i32.shr_s', None, 0
    I32_SHR_U = 0x76, 'i32.shr_u', None, 0
    I32_ROTL = 0x77, 'i32.rotl', None, 0
    I32_ROTR = 0x78, 'i32.rotr', None, 0
    I64_CLZ = 0x79, 'i64.clz', None, 0
    I64_CTZ = 0x7a, 'i64.ctz', None, 0
    I64_POPCNT = 0x7b, 'i64.popcnt', None, 0
    I64_ADD = 0x7c, 'i64.add', None, 0
    I64_SUB = 0x7d, 'i64.sub', None, 0
    I64_MUL = 0x7e, 'i64.mul', None, 0
    I64_DIV_S = 0x7f, 'i64.div_s', None, 0
    I64_DIV_U = 0x80, 'i64.div_u', None, 0
    I64_REM_S = 0x81, 'i64.rem_s', None, 0
    I64_REM_U = 0x82, 'i64.rem_u', None, 0
    I64_AND = 0x83, 'i64.and', None, 0
    I64_OR = 0x84, 'i64.or', None, 0
    I64_XOR = 0x85, 'i64.xor', None, 0
    I64_SHL = 0x86, 'i64.shl', None, 0
    I64_SHR_S = 0x87, 'i64.shr_s', None, 0
    I64_SHR_U = 0x88, 'i64.shr_u', None, 0
    I64_ROTL = 0x89, 'i64.rotl', None, 0
    I64_ROTR = 0x8a, 'i64.rotr', None, 0
    F32_ABS = 0x8b, 'f32.abs', None, 0
    F32_NEG = 0x8c, 'f32.neg', None, 0
    F32_CEIL = 0x8d, 'f32.ceil', None, 0
    F32_FLOOR = 0x8e, 'f32.floor', None, 0
    F32_TRUNC = 0x8f, 'f32.trunc', None, 0
    F32_NEAREST = 0x90, 'f32.nearest', None, 0
    F32_SQRT = 0x91, 'f32.sqrt', None, 0
    F32_ADD = 0x92, 'f32.add', None, 0
    F32_SUB = 0x93, 'f32.sub', None, 0
    F32_MUL = 0x94, 'f32.mul', None, 0
    F32_DIV = 0x95, 'f32.div', None, 0
    F32_MIN = 0x96, 'f32.min', None, 0
    F32_MAX = 0x97, 'f32.max', None, 0
    F32_COPYSIGN = 0x98, 'f32.copysign', None, 0
    F64_ABS = 0x99, 'f64.abs', None, 0
    F64_NEG = 0x9a, 'f64.neg', None, 0
    F64_CEIL = 0x9b, 'f64.ceil', None, 0
    F64_FLOOR = 0x9c, 'f64.floor', None, 0
    F64_TRUNC = 0x9d, 'f64.trunc', None, 0
    F64_NEAREST = 0x9e, 'f64.nearest', None, 0
    F64_SQRT = 0x9f, 'f64.sqrt', None, 0
    F64_ADD = 0xa0, 'f64.add', None, 0
    F64_SUB = 0xa1, 'f64.sub', None, 0
    F64_MUL = 0xa2, 'f64.mul', None, 0
    F64_DIV = 0xa3, 'f64.div', None, 0
    F64_MIN = 0xa4, 'f64.min', None, 0
    F64_MAX = 0xa5, 'f64.max', None, 0
    F64_COPYSIGN = 0xa6, 'f64.copysign', None, 0

    I32_WRAP_I64 = 0xa7, 'i32.wrap/i64', None, 0
    I32_TRUNC_S_F32 = 0xa8, 'i32.trunc_s/f32', None, 0
    I32_TRUNC_U_F32 = 0xa9, 'i32.trunc_u/f32', None, 0
    I32_TRUNC_S_F64 = 0xaa, 'i32.trunc_s/f64', None, 0
    I32_TRUNC_U_F64 = 0xab, 'i32.trunc_u/f64', None, 0
    I64_EXTEND_S_I32 = 0xac, 'i64.extend_s/i32', None, 0
    I64_EXTEND_U_I32 = 0xad, 'i64.extend_u/i32', None, 0
    I64_TRUNC_S_F32 = 0xae, 'i64.trunc_s/f32', None, 0
    I64_TRUNC_U_F32 = 0xaf, 'i64.trunc_u/f32', None, 0
    I64_TRUNC_S_F64 = 0xb0, 'i64.trunc_s/f64', None, 0
    I64_TRUNC_U_F64 = 0xb1, 'i64.trunc_u/f64', None, 0
    F32_CONVERT_S_I32 = 0xb2, 'f32.convert_s/i32', None, 0
    F32_CONVERT_U_I32 = 0xb3, 'f32.convert_u/i32', None, 0
    F32_CONVERT_S_I64 = 0xb4, 'f32.convert_s/i64', None, 0
    F32_CONVERT_U_I64 = 0xb5, 'f32.convert_u/i64', None, 0
    F32_DEMOTE_F64 = 0xb6, 'f32.demote/f64', None, 0
    F64_CONVERT_S_I32 = 0xb7, 'f64.convert_s/i32', None, 0
    F64_CONVERT_U_I32 = 0xb8, 'f64.convert_u/i32', None, 0
    F64_CONVERT_S_I64 = 0xb9, 'f64.convert_s/i64', None, 0
    F64_CONVERT_U_I64 = 0xba, 'f64.convert_u/i64', None, 0
    F64_PROMOTE_F32 = 0xbb, 'f64.promote/f32', None, 0

    I32_REINTERPRET_F32 = 0xbc, 'i32.reinterpret/f32', None, 0
    I64_REINTERPRET_F64 = 0xbd, 'i64.reinterpret/f64', None, 0
    F32_REINTERPRET_I32 = 0xbe, 'f32.reinterpret/i32', None, 0
    F64_REINTERPRET_I64 = 0xbf, 'f64.reinterpret/i64', None, 0

    def __new__(cls, opcode_id, mnemonic, imm_struct, flags):
        member = object.__new__(cls)
        member._value_ = opcode_id
        member.id = opcode_id
        member.mnemonic = mnemonic
        member.imm_struct = imm_struct
        member.flags = flags

        return member

    @classmethod
    def from_id(cls, opcode_id):
        result = [item for item in cls if item.value == opcode_id]
        if not result:
            raise Exception(f'No opcode found (opcode_id: {opcode_id})')
        return result[0]

