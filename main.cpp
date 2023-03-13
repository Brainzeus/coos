#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <openssl/ec.h>
#include <openssl/evp.h>
#include <openssl/bn.h>
#include <openssl/obj_mac.h>

int main() {
    // Exemplu de cheie publică în format hex
    std::string public_key_hex = "03c4eb4a4b4ad1a4b12f8c1fb72fa3b41a7e2f3730c8e7d249b6ebf9daec0f60c";

    // Transformăm cheia publică din format hex în octeți
    unsigned char public_key_bytes[65];
    size_t public_key_len = strlen(public_key_hex.c_str()) / 2;
    for (int i = 0; i < public_key_len; i++) {
        sscanf(public_key_hex.c_str() + 2*i, "%02x", &public_key_bytes[i]);
    }

    // Inițializăm curba SECP256k1
    EC_GROUP *group = EC_GROUP_new_by_curve_name(NID_secp256k1);

    // Inițializăm un punct pe curba SECP256k1 cu coordonatele 0,0
    EC_POINT *point = EC_POINT_new(group);

    // Setăm punctul cu coordonatele cheii publice
    int result = EC_POINT_oct2point(group, point, public_key_bytes, public_key_len, NULL);

    // Obținem coordonatele x și y ale punctului
    BIGNUM *x_bn = BN_new();
    BIGNUM *y_bn = BN_new();
    EC_POINT_get_affine_coordinates_GFp(group, point, x_bn, y_bn, NULL);

    // Transformăm coordonatele x și y în format hex
    char *x_hex = BN_bn2hex(x_bn);
    char *y_hex = BN_bn2hex(y_bn);

    // Afișăm coordonatele x și y în format hex
    std::cout << "Coordonate ECDSA x și y:" << std::endl;
    std::cout << "x: " << x_hex << std::endl;
    std::cout << "y: " << y_hex << std::endl;

    // Eliberăm memoria alocată
    EC_GROUP_free(group);
    EC_POINT_free(point);
    BN_free(x_bn);
    BN_free(y_bn);
    OPENSSL_free(x_hex);
    OPENSSL_free(y_hex);

    return 0;
}
