 // 给参数ids的门店添加True
 function _add_true_for_tree(ids, join_or_not){
    ids_array = ids.split(',')
     console.log(ids_array)
    for(var i=0; i<tree_data.length; i++){
        cur_market = tree_data[i];
        citys_array = cur_market.items;
        for(var j=0; j<citys_array.length; j++){
            cur_city = citys_array[j]
            districts_array = cur_city.items;
            for(var k=0; k<districts_array.length; k++){
                cur_district = districts_array[k]
                stores_array = cur_district.items
                for(var m=0; m<stores_array.length; m++){
                    cur_store = stores_array[m]
                    // 如果当前门店id在所填id数组中，且不参加活动
                    // $.inArray(cur_store.id, ids_array) != '-1'  表示在数组中
                    if($.inArray(cur_store.id, ids_array) != '-1'){
                        if (join_or_not == '2') {
                            cur_store.checked = true
                        } else {
                            delete cur_store.checked
                        }
                    // 如果当前门店id不在所填id数组中，且参加活动
                    }else{
                        if(join_or_not == '1'){
                            cur_store.checked = true
                        } else {
                            delete cur_store.checked
                        }
                    }

                }
            }

        }
    }
 }