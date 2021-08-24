const fs = require("fs")

module.exports.jsonGetquery = async () => {
    const resultJSONfile = fs.readFileSync("./resultJSON.json", 'utf8')
    return resultJSONfile;
}
