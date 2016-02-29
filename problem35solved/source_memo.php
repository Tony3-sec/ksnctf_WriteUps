<?php

function h($s)
{
    return htmlspecialchars($s, ENT_QUOTES, 'UTF-8');
}

if (!isset($_POST['id']) or !is_string($_POST['id']))
    $_POST['id'] = '';
if (!isset($_POST['password']) or !is_string($_POST['password']))
    $_POST['password'] = '';

$try = false;
$ok = false;

if ($_POST['id']!=='' or $_POST['password']!=='')
{
    $try = true;
    $db = new PDO('sqlite:database.db');
    $s = $db->prepare('SELECT * FROM user WHERE id=? AND password=?');
    $s->execute(array($_POST['id'], $_POST['password'])); //execute():  Executes a prepared statement. Returns TRUE on success or FALSE on failure. All values are treated as string.
    $ok = $s->fetch() !== false; //fetch(): Fetches the next row from a result set. The return value of this function on success depends on the fetch type. In all cases, FALSE is returned on failure.
}

?>
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Auth 2</title>
    <link rel="stylesheet" href="bootstrap.min.css">
    <style>
      body
      {
        padding: 40px;
        background: #eee;
      }
      .form-control
      {
        position: relative;
        font-size: 16px;
        height: auto;
        padding: 10px;
        box-sizing: border-box;
      }
      .form-control:focus
      {
        z-index: 2;
      }
      input[type="text"]
      {
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
      input[type="password"]
      {
        border-top-left-radius: 0;
        border-top-right-radius: 0;
      }
      button
      {
        margin-top: 16px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <form method="POST" style="width:320px; margin:auto">
        <h1>Simple Auth 2</h1>

<?php if($try and $ok) { ?>
        <div class="alert alert-success">
          Congraturation!<br>
          The flag is <?php echo h($_POST['password']); ?>
        </div>
<?php } ?>

<?php if ($try and !$ok) { ?>
        <div class="alert alert-danger">
          Incorrect ID or password
        </div>
<?php } ?>

<?php if (!$ok) { ?>
        <input
          type="text"
          class="form-control"
          id="id"
          name="id"
          placeholder="ID"
          value="<?php echo h($_POST['id']); ?>">
        <input
          type="password"
          class="form-control"
          id="password"
          name="password"
          placeholder="Password">
        <button
          class="btn btn-lg btn-primary btn-block"
          type="submit">
          Sign in
        </button>
<?php } ?>
      </form>
    </div>
  </body>
</html>