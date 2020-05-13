// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 

package info.sweetduet.ksnctf.jewel;

import android.app.Activity;
import android.content.res.Resources;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.widget.ImageView;
import android.widget.Toast;
import java.io.InputStream;
import java.math.BigInteger;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

// Referenced classes of package info.sweetduet.ksnctf.jewel:
//            b, a

public class JewelActivity extends Activity
{

    public JewelActivity()
    {
    }

    public void onCreate(Bundle bundle)
    {
        super.onCreate(bundle);
        setContentView(0x7f030000);
        bundle = ((TelephonyManager)getSystemService("phone")).getDeviceId();
        Object obj;
        obj = MessageDigest.getInstance("SHA-256");
        ((MessageDigest) (obj)).update(bundle.getBytes("ASCII"));
        BigInteger biginteger = JVM INSTR new #54  <Class BigInteger>;
        biginteger.BigInteger(((MessageDigest) (obj)).digest());
        obj = biginteger.toString(16);
        if(bundle.substring(0, 8).equals("99999991")) goto _L2; else goto _L1
_L1:
        bundle = JVM INSTR new #76  <Class android.app.AlertDialog$Builder>;
        bundle.android.app.AlertDialog.Builder(this);
        bundle = bundle.setMessage("Your device is not supported").setCancelable(false);
        obj = JVM INSTR new #91  <Class b>;
        ((b) (obj)).b(this);
        bundle.setPositiveButton("OK", ((android.content.DialogInterface.OnClickListener) (obj))).show();
_L3:
        return;
_L2:
label0:
        {
            if(((String) (obj)).equals("356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"))
                break label0;
            bundle = JVM INSTR new #76  <Class android.app.AlertDialog$Builder>;
            bundle.android.app.AlertDialog.Builder(this);
            bundle = bundle.setMessage("You are not a valid user").setCancelable(false);
            obj = JVM INSTR new #110 <Class a>;
            ((a) (obj)).a(this);
            bundle.setPositiveButton("OK", ((android.content.DialogInterface.OnClickListener) (obj))).show();
        }
          goto _L3
        try
        {
            Object obj1 = getResources().openRawResource(0x7f040000);
            byte abyte0[] = new byte[((InputStream) (obj1)).available()];
            ((InputStream) (obj1)).read(abyte0);
            obj1 = JVM INSTR new #144 <Class SecretKeySpec>;
            Object obj2 = JVM INSTR new #146 <Class StringBuilder>;
            ((StringBuilder) (obj2)).StringBuilder("!");
            ((SecretKeySpec) (obj1)).SecretKeySpec(((StringBuilder) (obj2)).append(bundle).toString().getBytes("ASCII"), "AES");
            obj2 = JVM INSTR new #163 <Class IvParameterSpec>;
            ((IvParameterSpec) (obj2)).IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
            bundle = Cipher.getInstance("AES/CBC/PKCS5Padding");
            bundle.init(2, ((java.security.Key) (obj1)), ((java.security.spec.AlgorithmParameterSpec) (obj2)));
            bundle = bundle.doFinal(abyte0);
            ImageView imageview = JVM INSTR new #185 <Class ImageView>;
            imageview.ImageView(this);
            imageview.setImageBitmap(BitmapFactory.decodeByteArray(bundle, 0, bundle.length));
            setContentView(imageview);
        }
        // Misplaced declaration of an exception variable
        catch(Bundle bundle)
        {
            Toast.makeText(this, bundle.toString(), 1).show();
        }
          goto _L3
    }
}
