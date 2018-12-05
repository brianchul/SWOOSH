<template>
  <div id="order">
    <div class="title">訂單管理</div>

    <el-table class="tbTitle" :data="orderData" height="380">
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form inline class="table-expand">
            <el-form-item label="進場日期：">
              <span>{{ props.row.toFactoryDate }}</span>
            </el-form-item>
            <el-form-item label="預算： $">
              <span>{{ props.row.budget }}</span>
            </el-form-item>
            <el-form-item label="此次目的：">
              <span>{{ props.row.purpose }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column label="衛星名稱" prop="name"></el-table-column>
      <el-table-column label="發射高度" prop="height"></el-table-column>
      <el-table-column label="發射傾角" prop="inclination"></el-table-column>
      <el-table-column label="衛星重量" prop="weight"></el-table-column>
      <el-table-column label="發射日期" prop="launchDate"></el-table-column>
      <el-table-column label="刊登日期" prop="createTime"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "Order",
  data() {
    return {
      orderData: [
        {
          name: "福衛66號",
          weight: "10Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/08/01",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "ComeOnNASA",
          weight: "15Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/10/21",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "Super Rocket",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/11/25",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "ComeOnNASA2",
          weight: "500Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2025/11/11",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "TKU",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2030/12/31",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "福衛66號",
          weight: "10Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/08/01",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "ComeOnNASA",
          weight: "15Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/10/21",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "Super Rocket",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2020/11/25",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "ComeOnNASA2",
          weight: "500Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2025/11/11",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        },
        {
          name: "TKU",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34度",
          launchDate: "2030/12/31",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01"
        }
      ]
    };
  }
};
</script>

<style scoped>
.title {
  color: #fff;
  font-size: 30px;
  padding-bottom: 10px;
}
.tbTitle {
  height: auto;
  border-radius: 8px;
  text-align: center;
}
</style>

<style>
#order .el-table th {
  font-size: 16px;
}
#order .table-expand label {
    width: 90px;
    color: #99a9bf;
  }
#order .table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 33%;
  }
</style>