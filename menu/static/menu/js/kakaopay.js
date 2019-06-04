$(document).ready(function(){

    $('#cart_total_button').click(function(){
    
         Kakao.API.request({
            url: '/v1/payment/ready',
            Authorization: 'KakaoAK {3f5b63af3e3b694fba0f2bbd4ad341ef}',
            cid: "TC0ONETIME",
            partner_order_id: 'partner_order_id',
            partner_user_id: 'partner_user_id',
            item_name: '라이언빵',
            quantity: '1',
            total_amount: '1000',
            vat_amount: '200',
            tax_free_amount: '0',
            approval_url: 'success.jsp',
            fail_url: 'fail.jsp',
            cancel_url: 'cancel.jsp',
            success: function(res) {
                  alert('성공');
            },
            fail: function(error) {
                  alert('실패');
            }
          }); 
          
        
    });
    });