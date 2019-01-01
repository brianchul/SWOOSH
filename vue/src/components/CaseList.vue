<template>
    <div>
        <div class='title'>
            已申請清單
        </div>
        <div class='separate'></div>
        <List :payload='needList' listName='need'/>
        <List :payload='saleList' listName='sale'/>
    </div>
</template>

<script>
import List from './CaseList/List.vue'
import api from '../lib/'
import moment from 'moment'

export default {
    name: 'CaseList',
    components: {
        List,
    },
    props: {
        userInfo: Object,
    },
    data() {
        return {
            needList: [],
            saleList: [],
        }
    },
    methods: {
        onFailed: function() {
            this.$message({
                type: 'error',
                message: 'data not found',
                center: true,
            })
        },
        getNeedOnSuccess: function(data) {
            data.map((item)=>{
                item.arrival_date = moment(new Date(item.arrival_date),'ddd, DD MMM YYYY').format('YYYY/MM/DD')
            })
            this.needList = data
        },
        getMissionOnSuccess: function(data) {
            data.map((item)=>{
                item.mission_arrival_deadline = moment(new Date(item.mission_arrival_deadline),'ddd, DD MMM YYYY').format('YYYY/MM/DD')
            })
            this.saleList = data
        },
    },
    created() {
        api.getAllNeeds(this.getNeedOnSuccess,this.onFailed)
        api.getAllMissionOrder(this.getMissionOnSuccess,this.onFailed)
    },
}
</script>

<style scoped>
.title {
    color: #fff;
    font-size: 30px;
    border-bottom: 2px solid #fff;
    padding-bottom: 10px;
}
.separate {
    width: 100%;
    height: 5px;
    border-bottom: 2px solid #fff;
}
.testBtn {
    width: 100%;
    height: 100px;
    background-color: red;
    border-radius: 10px;
}
</style>