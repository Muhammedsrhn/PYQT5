
// describe("us", function(){




//   it("2 ** 2", function(){
//     assert.equal(us(2,2),8);
//   });

//   it("2 ** 3", function(){
//     assert.equal(us(2,3),81);
//   });

//   it("2 ** 3", function(){
//     assert.equal(us(1,1),1);
//   });
  
//   // it("3 * 3", function(){
//   //   assert.equal(us(3,3),27);
//   // })
    
// });

// mocha.run();


describe("us1", function(){

describe("us2", function(){

    function testEt(x){
      let beklenen = x*x*x;
      it(`${x} 3. kuvveti ${beklenen}'dir`, function(){
          assert.equal(us(x,3),beklenen)
      });
    
    for (let x = 0;x < 5 ; x++){
      testEt(x);
    }
  }
});
});

// describe("test", function(){
//         after(() => {alert("After fonksiyon calıstırıldı.")});
//         before(() => {alert("Before fonksiyon calıstırıldı.")});
//         beforeEach(() => {alert("BeforeEach fonksiyon calıstırıldı.")});
//         afterEach(() => {alert("AfterEach fonksiyon calıstırıldı.")});

//         it('test1',() => alert(1));
//         it('test2',() => alert(2));
// });



// describe("us1", function(){
//     it("us control1", function(){
//         assert.isNaN(us( 2,-1));
//     });
// });

// describe("us2", function(){
//   it("us control2", function(){
//       assert.isNaN(us( 2,1.5));
//   });
// });

describe("bdd", function(){
    it("bdd", function(){
      assert.isNaN(us(2,1.2));
  });
});