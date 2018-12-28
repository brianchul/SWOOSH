<template>
  <div id="order">
    <div class="title">訂單管理</div>
    <template v-if="userInfo.permission === 'user'">
      <el-table class="tbTitle" :data="showneedData" height="380" key="Need" empty-text="目前無已申請之訂單">
        <el-table-column type="expand">
          <template slot-scope="nprops">
            <el-form inline class="table-expand">
              <el-form-item label="進廠日期：">
                <span>{{ nprops.row.arrival_date }}</span>
              </el-form-item>
              <el-form-item label="預算： $">
                <span>{{ nprops.row.budget_billion }}</span>
              </el-form-item>
              <el-form-item label="此次目的：">
                <span>{{ nprops.row.purpose }}</span>
              </el-form-item>
              <!-- <el-form-item label="id：">
                <span>{{ nprops.row.id }}</span>
              </el-form-item>-->
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="衛星名稱" prop="satellite_name"></el-table-column>
        <el-table-column label="發射高度" prop="eta_height_km"></el-table-column>
        <el-table-column label="發射傾角" prop="inclination"></el-table-column>
        <el-table-column label="衛星重量" prop="weight_kg"></el-table-column>
        <el-table-column label="發射日期" prop="launch_day"></el-table-column>
        <el-table-column label="刊登日期" prop="created_time"></el-table-column>
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
            <el-tooltip class="item" effect="dark" content="編輯" placement="right">
              <el-button
                icon="el-icon-edit"
                type="info"
                circle
                @click="showNeedOverlay(scope.$index)"
              ></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog title="訂單編輯" :visible.sync="NisActive">
        <el-form :model="selectedNeedlist" label-position="right" label-width="90px">
          <el-form-item label="衛星名稱：">
            <el-input v-model="selectedNeedlist.satellite_name" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射高度：">
            <el-select v-model="selectedNeedlist.eta_height_km" placeholder="請選擇軌道高度">
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
            <el-input v-model="selectedNeedlist.weight_kg" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射日期：">
            <el-date-picker
              v-model="selectedNeedlist.launch_day"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="進廠日期：">
            <el-date-picker
              v-model="selectedNeedlist.arrival_date"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="預算：">
            <el-input v-model="selectedNeedlist.budget_billion" autocomplete="off" clearable></el-input>
          </el-form-item>
          <!-- <el-form-item label="id：">
              <el-input v-model="selectedNeedlist.id" autocomplete="off" clearable></el-input>
          </el-form-item>-->
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
      <el-table class="tbTitle" :data="showrocketData" key="Rocket" empty-text="目前無已上傳之火箭">
        <el-table-column type="expand">
          <!-- <template slot-scope="props">
            <el-form inline class="table-expand">
              <el-form-item label="已配對衛星：">
                <span v-for="(item, index) in props.row.pair_order">{{item.satellite_name}}</span>
              </el-form-item>
               <el-form-item label="已販售機位：">
                <span>{{ props.row.saleList }}</span>
              </el-form-item>
            </el-form>
          </template>  -->
        </el-table-column>
        <el-table-column label="火箭ID" prop="id"></el-table-column>
        <el-table-column label="火箭名稱" prop="launch_rocket"></el-table-column>
        <el-table-column label="發射高度" prop="target_height_km"></el-table-column>
        <el-table-column label="發射傾角" prop="target_inclination"></el-table-column>
        <el-table-column label="限重" prop="rocket_max_payload_weight"></el-table-column>
        <el-table-column label="發射日期" prop="launch_date"></el-table-column>
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
            <el-button icon="el-icon-edit" type="info" circle @click="showOverlay(scope.$index)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="title2">。機位</div>
      <el-table class="tbTitle" :data="showsaleData" key="Sale" empty-text="目前無已上傳之機位">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form inline class="table-expand">
              <el-form-item label="訂購者：">
                <span>{{ props.row.clientName }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="火箭ID" prop="mission_id"></el-table-column>
        <el-table-column label="限重" prop="limit_weight"></el-table-column>
        <el-table-column label="最晚進廠日" prop="mission_arrival_deadline"></el-table-column>
        <el-table-column label="售價" prop="seat_price"></el-table-column>
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
        <el-form :model="selectedlist" label-position="right" label-width="150px">
          <el-form-item label="火箭名稱：">
            <el-input v-model="selectedlist.launch_rocket" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射高度：">
            <el-select v-model="selectedlist.target_height_km" placeholder="請選擇軌道高度">
              <el-option label="Low-Earth Orbit" value="LEO"></el-option>
              <el-option label="Medium-Earth Orbit" value="MEO"></el-option>
              <el-option label="Geostationary Orbit" value="GEO"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="發射傾角：">
            <el-select v-model="selectedlist.target_inclination" placeholder="請選擇發射傾角">
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
            <el-input v-model="selectedlist.rocket_max_payload_weight" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="發射日期：">
            <el-date-picker
              v-model="selectedlist.launch_date"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
           <!-- <el-form-item label="已配對之衛星ID：">
            <el-input v-model="selectedlist.pairOrderId" autocomplete="off" clearable></el-input>
          </el-form-item>  -->
          <el-form-item label="狀態：">
            <el-switch v-model="selectedlist.status" active-text="開放中" inactive-text="關閉"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="changeOverlay">取消</el-button>
          <el-button type="primary" @click="modify_R(selectedlist)">儲存</el-button>
        </div>
      </el-dialog>
      <el-dialog title="機位編輯" :visible.sync="SisActive">
        <el-form :model="selectedSalelist" label-position="right" label-width="150px">
          <el-form-item label="火箭ID：">
            <el-input v-model="selectedSalelist.mission_id" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="限重：">
            <el-input v-model="selectedSalelist.limit_weight" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="最晚進廠日：">
            <el-date-picker
              v-model="selectedSalelist.mission_arrival_deadline"
              type="date"
              value-format="yyyy-MM-dd"
              placeholder="請選擇日期"
            ></el-date-picker>
          </el-form-item>
          <el-form-item label="售價：">
            <el-input v-model="selectedSalelist.seat_price" autocomplete="off" clearable></el-input>
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
import api from "../lib/";
import moment from "moment";

export default {
  name: "Order",
  props: {
    userInfo: Object
  },
  data() {
    return {
      needData: [],
      saleData: [],
      rocketData: [],
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
      showOrder: []
    };
  },
  created() {
    const info = JSON.parse(localStorage.getItem("userInfo"));
    if (!info.is_launch_company) {
      api.getAllNeeds(this.selectNSuccess, this.getOnFailed);
      //const needInfo = JSON.parse(localStorage.getItem("needInfo"));
      //this.needData = needInfo;
    } else {
      api.getAllMission(this.selectMSuccess, this.getOnFailed);
      api.getAllMissionOrder(this.selectMOSuccess, this.getOnFailed);
      // const missoninfo = JSON.parse(localStorage.getItem("missionInfo"));
       const missonOrderinfo = JSON.parse(
         localStorage.getItem("missionOrderInfo")
       );
      //console.log(missoninfo);
      // this.setSrocket(missoninfo);
       this.setSsale(missonOrderinfo);
    }
  },
  methods: {
    setSrocket(arr) {
      this.showrocketData = JSON.parse(JSON.stringify(arr));
      if (this.showrocketData != null) {
        this.showrocketData.forEach(element => {
          element.launch_date = this.dateReviver(element.launch_date);
          if (element.status == 1) {
            element.status = true;
          } else {
            element.status = false;
          }
          //  if (element.pair_order != null) {
          //    element.pair_order.forEach(o =>{
          //      element.pairOrderId = JSON.stringify(o.id);
          //      element.pairOrderId += ",";
          //    })
          //   //  api.getNeedById(element.pair_order,this.getNeedByIdSuccess, this.getOnFailed);
          //   //  const getOneNeedInfo = JSON.parse(localStorage.getItem("getOneNeedInfo"));
          //    console.log("pair_order:");
          //    console.log(element.pairOrderId);
          //    //element.satellite_name = getOneNeedInfo.satellite_name;
          //  }
        });
      }
    },
    showOverlay(index) {
      this.selected = index;
      //const missoninfo = JSON.parse(localStorage.getItem("missionInfo"));
      this.selectedlist = JSON.parse(
        JSON.stringify(this.showrocketData[index])
      );
      this.changeOverlay();
    },
    changeOverlay() {
      this.RisActive = !this.RisActive;
    },
    //點選儲存
    modify_R(arr) {
      if (this.selected > -1) {
        Vue.set(this.showrocketData, this.selected, arr);
        this.selected = -1;
      } else {
        this.rocketData.push(arr);
      }
      this.setSrocket(this.showrocketData);
      api.patchMission(arr, this.patchOnSuccess, this.patchOnFailed);
      this.changeOverlay();
    },

    setSsale(arr) {
      this.showsaleData = JSON.parse(JSON.stringify(arr));
      if (this.showsaleData != null) {
        this.showsaleData.forEach(element => {
          element.mission_arrival_deadline = this.dateReviver(
            element.mission_arrival_deadline
          );
          if (element.status == 1) {
            element.status = true;
          } else {
            element.status = false;
          }
          if (element.order_id != null) {
            api.getClientById(element.order_id,this.getClientByIdSuccess, this.getOnFailed);
            const clientInfo = JSON.parse(localStorage.getItem("clientInfo"));
            element.clientName = clientInfo.name;
          }
        });
      }
    },
    showSaleOverlay(index) {
      this.selected = index;
      //const missonOrderinfo = JSON.parse(localStorage.getItem("missionOrderInfo"));
      this.selectedSalelist = JSON.parse(
        JSON.stringify(this.showsaleData[index])
      );
      this.changeSaleOverlay();
    },
    changeSaleOverlay() {
      this.SisActive = !this.SisActive;
    },
    // 點選儲存
    modify_S(arr) {
      if (this.selected > -1) {
        Vue.set(this.showsaleData, this.selected, arr);
        this.selected = -1;
      } else {
        this.saleData.push(arr);
      }
      this.setSsale(this.showsaleData);
      api.patchMissionOrder(arr, this.patchOnSuccess, this.patchOnFailed);
      this.changeSaleOverlay();
    },

    setNsale(arr) {
      this.showneedData = JSON.parse(JSON.stringify(arr));
      this.showneedData.forEach(element => {
        element.arrival_date = this.dateReviver(element.arrival_date);
        element.launch_day = this.dateReviver(element.launch_day);
        element.created_time = this.dateReviver(element.created_time);
        if (element.status == 1) {
          element.status = true;
        } else {
          element.status = false;
        }
      });
    },
    showNeedOverlay(index) {
      this.selected = index;
      this.selectedNeedlist = JSON.parse(
        JSON.stringify(this.showneedData[index])
      );
      this.changeNeedOverlay();
    },
    changeNeedOverlay() {
      this.NisActive = !this.NisActive;
    },
    // 點選儲存
    modify_N(arr) {
      if (this.selected > -1) {
        Vue.set(this.showneedData, this.selected, arr);
        this.selected = -1;
      } else {
        this.needData.push(arr);
      }
      this.setNsale(this.showneedData);
      api.patchNeed(arr, this.patchOnSuccess, this.patchOnFailed);
      this.changeNeedOverlay();
    },
    patchOnSuccess: function() {
      this.$message({
        message: "儲存成功！",
        type: "success",
        center: true
      });
    },
    patchOnFailed: function() {
      this.$message({
        type: "error",
        message: "儲存失敗，請重新確認",
        center: true
      });
    },
    getOnFailed: function() {
      this.$message({
        type: "error",
        message: "取資料失敗，請重新確認",
        center: true
      });
    },
    selectMSuccess: function(data) {
      //localStorage.setItem("missionInfo", JSON.stringify(data));
      this.rocketData = JSON.parse(JSON.stringify(data));
      this.setSrocket(this.rocketData);
    },
    selectMOSuccess: function(data) {
      localStorage.setItem("missionOrderInfo", JSON.stringify(data));
      // this.saleData = JSON.parse(JSON.stringify(data));
      // console.log("saleData");
      // this.setSsale(this.saleData);
    },
    selectNSuccess: function(data) {
      // console.log("資料庫回傳");
      // console.log(data);
      //localStorage.setItem(this.needData, JSON.parse(JSON.stringify(data)));
      this.needData = JSON.parse(JSON.stringify(data));
      this.setNsale(this.needData);
    },
    getClientByIdSuccess: function(data) {
      localStorage.setItem("clientInfo", JSON.stringify(data));
    },
    getNeedByIdSuccess: function(data) {
      localStorage.setItem("getOneNeedInfo", JSON.stringify(data));
    },
    dateReviver: function(value) {
      if (typeof value === "string") {
        this.test = moment(new Date(value), "ddd, DD MMM YYYY").format(
          "YYYY/MM/DD"
        );
        return moment(new Date(value), "ddd, DD MMM YYYY").format("YYYY/MM/DD");
      }
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