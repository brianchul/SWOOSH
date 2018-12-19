<template>
  <div id="order">
    <div class="title">訂單管理</div>
    <template v-if="userInfo.permission === 'user'">
      <el-table class="tbTitle" :data="showneedData" height="380" key="Need">
        <el-table-column type="expand">
          <template slot-scope="nprops">
            <el-form inline class="table-expand">
              <el-form-item label="進場日期：">
                <span>{{ nprops.row.toFactoryDate }}</span>
              </el-form-item>
              <el-form-item label="預算： $">
                <span>{{ nprops.row.budget }}</span>
              </el-form-item>
              <el-form-item label="此次目的：">
                <span>{{ nprops.row.purpose }}</span>
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
        <el-table-column label="狀態">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.status ? 'primary' : 'danger'"
              disable-transitions
            >{{scope.row.status ? "開放中" : "已關閉"}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope"><el-tooltip class="item" effect="dark" content="編輯" placement="right">
            <el-button
              icon="el-icon-edit"
              type="info"
              circle
              @click="showNeedOverlay(scope.$index)"
            ></el-button></el-tooltip>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="訂單編輯" :visible.sync="NisActive">
        <el-form :model="selectedNeedlist" :label-position="right" label-width="90px">
          <el-form-item label="衛星名稱：">
            <el-input v-model="selectedNeedlist.name" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射高度：">
            <el-select v-model="selectedNeedlist.height" placeholder="請選擇軌道高度">
              <el-option label="Low-Earth Orbit" value="LEO"></el-option>
              <el-option label="Medium-Earth Orbit" value="MEO"></el-option>
              <el-option label="Geostationary Orbit" value="GEO"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="發射傾角：">
            <el-select v-model="selectedNeedlist.inclination" placeholder="請選擇發射傾角">
              <el-option label="5~14度" value="5~14"></el-option>
              <el-option label="15~24度" value="15~24"></el-option>
              <el-option label="25~34度" value="25~34"></el-option>
              <el-option label="35~44度" value="35~44"></el-option>
              <el-option label="45~54度" value="45~54"></el-option>
              <el-option label="55~64度" value="55~64"></el-option>
              <el-option label="65~74度" value="65~74"></el-option>
              <el-option label="75~84度" value="75~84"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="衛星重量：">
            <el-input v-model="selectedNeedlist.weight" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射日期：">
            <el-date-picker v-model="selectedNeedlist.launchDate" type="date" placeholder="請選擇日期"></el-date-picker>
          </el-form-item>
          <el-form-item label="進場日期：">
            <el-date-picker
              v-model="selectedNeedlist.toFactoryDate"
              type="date"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="預算：">
            <el-input v-model="selectedNeedlist.budget" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="此次目的：">
            <el-input
              type="textarea"
              v-model="selectedNeedlist.purpose"
              autocomplete="off"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item label="狀態：">
            <el-switch v-model="selectedNeedlist.status" active-text="開放中" inactive-text="關閉"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeNeedOverlay">取消</el-button>
          <el-button type="primary" @click="modify_N(selectedNeedlist)">儲存</el-button>
        </div>
      </el-dialog>
    </template>
    <template v-else>
      <div class="title2">。火箭</div>
      <el-table class="tbTitle" :data="showrocketData" key="Rocket">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form inline class="table-expand">
              <el-form-item label="已配對衛星：">
                <span>{{ props.row.needList }}</span>
              </el-form-item>
              <el-form-item label="已販售機位：">
                <span>{{ props.row.saleList }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="火箭名稱" prop="rocketName"></el-table-column>
        <el-table-column label="發射高度" prop="height"></el-table-column>
        <el-table-column label="發射傾角" prop="Inclination"></el-table-column>
        <el-table-column label="限重" prop="totalWeight"></el-table-column>
        <el-table-column label="發射日期" prop="launchDate"></el-table-column>
        <el-table-column label="狀態">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.Status ? 'primary' : 'danger'"
              disable-transitions
            >{{scope.row.Status ? "開放中" : "已關閉"}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <el-button icon="el-icon-edit" type="info" circle @click="showOverlay(scope.$index)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="title2">。機位</div>
      <el-table class="tbTitle" :data="showsaleData" key="Sale">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form inline class="table-expand">
              <el-form-item label="訂購者：">
                <span>{{ props.row.useId }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="火箭名稱" prop="missionId"></el-table-column>
        <el-table-column label="限重" prop="limitWeight"></el-table-column>
        <el-table-column label="最晚進廠日" prop="lastFactoryDate"></el-table-column>
        <el-table-column label="售價" prop="price"></el-table-column>
        <el-table-column label="狀態">
          <template slot-scope="scope">
            <el-tag
              :type="scope.row.status ? 'primary' : 'danger'"
              disable-transitions
            >{{scope.row.status ? "開放中" : "已關閉"}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <el-button
              icon="el-icon-edit"
              type="info"
              circle
              @click="showSaleOverlay(scope.$index)"
            ></el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="火箭編輯" :visible.sync="RisActive">
        <el-form :model="selectedlist" :label-position="right" label-width="90px">
          <el-form-item label="火箭名稱：">
            <el-input v-model="selectedlist.rocketName" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射高度：">
            <el-select v-model="selectedlist.height" placeholder="請選擇軌道高度">
              <el-option label="Low-Earth Orbit" value="LEO"></el-option>
              <el-option label="Medium-Earth Orbit" value="MEO"></el-option>
              <el-option label="Geostationary Orbit" value="GEO"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="發射傾角：">
            <el-select v-model="selectedlist.Inclination" placeholder="請選擇發射傾角">
              <el-option label="5~14度" value="5~14"></el-option>
              <el-option label="15~24度" value="15~24"></el-option>
              <el-option label="25~34度" value="25~34"></el-option>
              <el-option label="35~44度" value="35~44"></el-option>
              <el-option label="45~54度" value="45~54"></el-option>
              <el-option label="55~64度" value="55~64"></el-option>
              <el-option label="65~74度" value="65~74"></el-option>
              <el-option label="75~84度" value="75~84"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="限重：">
            <el-input v-model="selectedlist.totalWeight" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射日期：">
            <el-date-picker v-model="selectedlist.launchDate" type="date" placeholder="請選擇日期"></el-date-picker>
          </el-form-item>
          <el-form-item label="狀態：">
            <el-switch v-model="selectedlist.Status" active-text="開放中" inactive-text="關閉"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeOverlay">取消</el-button>
          <el-button type="primary" @click="modify_R(selectedlist)">儲存</el-button>
        </div>
      </el-dialog>
      <el-dialog title="機位編輯" :visible.sync="SisActive">
        <el-form :model="selectedSalelist" :label-position="right" label-width="90px">
          <el-form-item label="火箭名稱：">
            <el-input v-model="selectedSalelist.missionId" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="限重：">
            <el-input v-model="selectedSalelist.limitWeight" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="最晚進廠日：">
            <el-date-picker
              v-model="selectedSalelist.lastFactoryDate"
              type="date"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="售價：">
            <el-input v-model="selectedSalelist.price" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="狀態：">
            <el-switch v-model="selectedSalelist.status" active-text="開放中" inactive-text="關閉"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeSaleOverlay">取消</el-button>
          <el-button type="primary" @click="modify_S(selectedSalelist)">儲存</el-button>
        </div>
      </el-dialog>
    </template>
  </div>
</template>

<script>
import Vue from "vue";
export default {
  name: "Order",
  props: {
    userInfo: Object
  },
  data() {
    return {
      needData: [
        {
          name: "福衛66號",
          weight: "10Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/08/01",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "ComeOnNASA",
          weight: "15Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/10/21",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: false
        },
        {
          name: "Super Rocket",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/11/25",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "ComeOnNASA2",
          weight: "500Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2025/11/11",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "TKU",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2030/12/31",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "福衛66號",
          weight: "10Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/08/01",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "ComeOnNASA",
          weight: "15Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/10/21",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "Super Rocket",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2020/11/25",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "ComeOnNASA2",
          weight: "500Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2025/11/11",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        },
        {
          name: "TKU",
          weight: "1000Kg",
          height: "LEO",
          inclination: "25~34",
          launchDate: "2030/12/31",
          toFactoryDate: "2019/12/20",
          budget: 1200,
          purpose: "test12 test123",
          createTime: "2018/08/01",
          status: true
        }
      ],
      saleData: [
        {
          missionId: "福衛66號",
          limitWeight: "10Kg",
          lastFactoryDate: "2019/12/20",
          price: 1200,
          status: true
        }
      ],
      rocketData: [
        {
          rocketName: "福衛66號",
          height: "LEO",
          Inclination: "25~34",
          totalWeight: "123",
          launchDate: "2020/08/01",
          Status: true
        },
        {
          rocketName: "福衛87號",
          height: "LEO",
          Inclination: "25~34",
          totalWeight: "123",
          launchDate: "2020/08/01",
          Status: false
        }
      ],
      showrocketData: [],
      showsaleData: [],
      showneedData: [],
      selected: -1,
      selectedlist: {},
      selectedSalelist: {},
      selectedNeedlist: {},
      RisActive: false,
      SisActive: false,
      NisActive: false,
    };
  },
  created() {
    this.setSrocket(this.rocketData);
    this.setSsale(this.saleData);
    this.setNsale(this.needData);
  },
  methods: {
    setSrocket(arr) {
      this.showrocketData = JSON.parse(JSON.stringify(arr));
    },
    showOverlay(index) {
      this.selected = index;
      this.selectedlist = JSON.parse(JSON.stringify(this.rocketData[index]));
      this.changeOverlay();
    },
    changeOverlay() {
      this.RisActive = !this.RisActive;
    },
    //點選儲存
    modify_R(arr) {
      if (this.selected > -1) {
        Vue.set(this.rocketData, this.selected, arr);
        this.selected = -1;
      } else {
        this.rocketData.push(arr);
      }
      this.setSrocket(this.rocketData);
      this.changeOverlay();
    },

    setSsale(arr) {
      this.showsaleData = JSON.parse(JSON.stringify(arr));
    },
    showSaleOverlay(index) {
      this.selected = index;
      this.selectedSalelist = JSON.parse(JSON.stringify(this.saleData[index]));
      this.changeSaleOverlay();
    },
    changeSaleOverlay() {
      this.SisActive = !this.SisActive;
    },
    // 點選儲存
    modify_S(arr) {
      if (this.selected > -1) {
        Vue.set(this.saleData, this.selected, arr);
        this.selected = -1;
      } else {
        this.saleData.push(arr);
      }
      this.setSsale(this.saleData);
      this.changeSaleOverlay();
    },

    setNsale(arr) {
      this.showneedData = JSON.parse(JSON.stringify(arr));
    },
    showNeedOverlay(index) {
      this.selected = index;
      this.selectedNeedlist = JSON.parse(JSON.stringify(this.needData[index]));
      this.changeNeedOverlay();
    },
    changeNeedOverlay() {
      this.NisActive = !this.NisActive;
    },
    // 點選儲存
    modify_N(arr) {
      if (this.selected > -1) {
        Vue.set(this.needData, this.selected, arr);
        this.selected = -1;
      } else {
        this.needData.push(arr);
      }
      this.setNsale(this.needData);
      this.changeNeedOverlay();
      this.$message({
        message: "儲存成功！",
        type: "success",
        center: true
      });
    }
  }
};
</script>

<style scoped>
.title {
  color: #fff;
  font-size: 30px;
  padding-bottom: 10px;
}
.title2 {
  color: #fff;
  font-size: 15px;
  padding-bottom: 5px;
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
  width: 100px;
  color: #99a9bf;
}
#order .table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 40%;
}
</style>