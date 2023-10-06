function mostcommon(arr) {
    let freq_counter = {}

    for (let val in arr) {
        freq_counter[val] = ((freq_counter[val] || 0) + 1)
    }

    console.log(freq_counter);
}

mostcommon(["Dean","lia","lia","danny","lia","lori","larson"]) // (2,3)