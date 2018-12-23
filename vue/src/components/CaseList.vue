<template>
    <div>
        <div class='title'>
            已申請清單
        </div>
        <div class='separate'></div>
        <List :payload='needList' listName='need'/>
        <List :payload='saleList' listName='sale'/>
        <button @click='test'>click</button>
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
            needsList: [],
            needList: [
                {
                    name: '福衛66號',
                    weight: '10Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/08/01',
                },
                {
                    name: 'ComeOnNASA',
                    weight: '15Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/10/21',
                },
                {
                    name: 'Super Rocket',
                    weight: '1000Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/11/25',
                },
                {
                    name: 'ComeOnNASA2',
                    weight: '500Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2025/11/11',
                },
                {
                    name: 'TKU',
                    weight: '1000Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2030/12/31',
                },
                {
                    name: '福衛66號',
                    weight: '10Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/08/01',
                },
                {
                    name: 'ComeOnNASA',
                    weight: '15Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/10/21',
                },
                {
                    name: 'Super Rocket',
                    weight: '1000Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2020/11/25',
                },
                {
                    name: 'ComeOnNASA2',
                    weight: '500Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2025/11/11',
                },
                {
                    name: 'TKU',
                    weight: '1000Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    launchDate: '2030/12/31',
                },
            ],
            saleList: [
                {
                    launchDate: '2018/12/31',
                    limitWeight: '50Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    price: '$50000',
                },
                {
                    launchDate: '2020/12/25',
                    limitWeight: '100Kg',
                    height: 'MEO',
                    inclination: '25~34度',
                    price: '$50000',
                },
                {
                    launchDate: '2021/01/01',
                    limitWeight: '500Kg',
                    height: 'HEO',
                    inclination: '25~34度',
                    price: '$90000',
                },
                {
                    launchDate: '2022/11/31',
                    limitWeight: '50Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    price: '$30000',
                },
                {
                    launchDate: '2025/10/10',
                    limitWeight: '1000Kg',
                    height: 'MEO',
                    inclination: '25~34度',
                    price: '$500000',
                },
                {
                    launchDate: '2030/12/31',
                    limitWeight: '5000Kg',
                    height: 'HEO',
                    inclination: '25~34度',
                    price: '$100000',
                },
                {
                    launchDate: '2050/12/31',
                    limitWeight: '10Kg',
                    height: 'LEO',
                    inclination: '25~34度',
                    price: '$10000',
                },
            ],
        }
    },
    methods: {
        test: function() {
            // api.getAllNeeds(this.onSuccess,this.onFailed)
        },
        onSuccess: function(data) {
            data.map((item) => {
                var date = moment(new Date(item.arrival_date),'ddd, DD MMM YYYY').format('YYYY/MM/DD')
                console.log(date)
            })
        },
        onFailed: function() {
            this.$message({
                type: 'error',
                message: 'not found',
                center: true,
            })
        }
    },
    created() {
        api.getAllNeeds(this.onSuccess,this.onFailed)
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