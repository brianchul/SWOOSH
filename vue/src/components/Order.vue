<template>
    <div>
        Order
        <el-table :data="" class="tbTitle">
          <el-table-column label="日期"></el-table-column>
          <el-table-column label="重量"></el-table-column>
          <el-table-column label="高度"></el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: 'Order',
}
</script>

<style scoped>
    .tbTitle{
        height: 200px;
        border-radius: 4px;
    }
</style>