//method 1
//find duplicates in collection
db.collection1.aggregate([
    {
        $group: {
        _id: {student: "$student", course: "$course"}, count: {$sum: 1}

        }
    },
    {
        $match: {
            count: {$gt: 1}
        }
    }
])

//create unique index in other collection
db.getCollection("collection2").createIndex({ "student": 1, "course": 1 }, {
    "unique": true,
    "background": true
})

//method 2
//remove duplicates in same collection
var docs = db.collection1.aggregate([
  {
    $group: {
      _id: {
          student: "$student",
          course: "$course"
      },
      uniqueIds: {
        $addToSet: "$_id"
      },
      count: {
        $sum: 1
      }
    }
  },
  {
    $match: {
      count: {
        $gt: 1
      }
    }
  }
]);

docs.forEach(function (doc) {
  doc.uniqueIds.shift();
  db.collection1.deleteMany({
    _id: {
      $in: doc.uniqueIds
    }
  });
});